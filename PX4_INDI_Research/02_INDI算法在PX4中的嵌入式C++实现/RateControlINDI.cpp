#include "RateControlINDI.hpp"
#include <px4_platform_common/defines.h>
#include <drivers/drv_hrt.h>

namespace px4
{
namespace control
{

RateControlINDI::RateControlINDI() :
	ModuleParams(nullptr),
	ScheduledWorkItem(MODULE_NAME, px4::wq_configurations::rate_ctrl)
{
	update_params();
}

RateControlINDI::~RateControlINDI()
{
	ScheduleClear();
}

bool RateControlINDI::init()
{
	// 绑定回调：一旦有新的角速度数据到达，立即触发运行
	if (!_vehicle_angular_velocity_sub.registerCallback()) {
		PX4_ERR("Failed to register angular velocity callback");
		return false;
	}

	return true;
}

void RateControlINDI::update_params()
{
	ModuleParams::updateParams();

	// 根据参数重新配置二阶滤波器截止频率
	const float cutoff = _param_indi_filt_cutoff.get();
	const float sample_rate = 500.0f; // 典型 500Hz 控制回路

	_ang_accel_filter.set_cutoff_frequency(sample_rate, cutoff);
	_actuator_filter.set_cutoff_frequency(sample_rate, cutoff);
}

void RateControlINDI::Run()
{
	if (should_exit()) {
		_vehicle_angular_velocity_sub.unregisterCallback();
		exit_and_cleanup();
		return;
	}

	// 检查参数更新
	if (_parameter_update_sub.updated()) {
		parameter_update_s param_update;
		_parameter_update_sub.copy(&param_update);
		update_params();
	}

	// 读取角速度数据
	vehicle_angular_velocity_s angular_velocity_msg;
	if (!_vehicle_angular_velocity_sub.update(&angular_velocity_msg)) {
		return;
	}

	// 检查控制模式
	vehicle_control_mode_s control_mode;
	if (_vehicle_control_mode_sub.copy(&control_mode)) {
		_is_active = control_mode.flag_control_rates_enabled;
	}

	if (!_is_active || !_param_indi_enable.get()) {
		// 未使能时重置历史状态
		_last_run_timestamp = angular_velocity_msg.timestamp;
		_last_angular_velocity = matrix::Vector3f(angular_velocity_msg.xyz);
		_last_torque_cmd.zero();
		_ang_accel_filter.reset();
		_actuator_filter.reset();
		return;
	}

	// 计算采样时间 dt
	const uint64_t now = angular_velocity_msg.timestamp;
	float dt = (now - _last_run_timestamp) * 1e-6f;
	_last_run_timestamp = now;

	if (dt <= 0.0001f || dt > 0.02f) {
		dt = 0.002f; // 异常时回退到默认 500Hz
	}

	compute_indi_torque(dt);
}

void RateControlINDI::compute_indi_torque(float dt)
{
	// 1. 获取当前角速度测量值
	vehicle_angular_velocity_s ang_vel_msg;
	_vehicle_angular_velocity_sub.copy(&ang_vel_msg);
	const matrix::Vector3f ang_vel(ang_vel_msg.xyz);

	// 2. 提取角加速度并进行二阶巴特沃斯低通滤波
	const matrix::Vector3f raw_ang_accel = (ang_vel - _last_angular_velocity) / dt;
	_last_angular_velocity = ang_vel;
	const matrix::Vector3f filtered_ang_accel = _ang_accel_filter.update(raw_ang_accel);

	// 3. 执行器指令对称滤波 (时间对齐关键步骤)
	const matrix::Vector3f filtered_actuator_torque = _actuator_filter.update(_last_torque_cmd);

	// 4. 获取期望角速度指令
	vehicle_rates_setpoint_s rates_sp_msg{};
	matrix::Vector3f rates_sp(0.0f, 0.0f, 0.0f);
	if (_vehicle_rates_setpoint_sub.update(&rates_sp_msg)) {
		rates_sp = matrix::Vector3f(rates_sp_msg.roll, rates_sp_msg.pitch, rates_sp_msg.yaw);
	}

	// 5. 计算虚拟角加速度输入 ν (Virtual Control Input)
	const matrix::Vector3f rate_error = rates_sp - ang_vel;
	const matrix::Vector3f kp(_param_indi_rate_p_x.get(), _param_indi_rate_p_y.get(), _param_indi_rate_p_z.get());
	const matrix::Vector3f virtual_accel = rate_error.emult(kp); // ν = Kp * e_ω

	// 6. 构造转动惯量矩阵 J
	const matrix::Vector3f inertia_diag(_param_indi_inertia_x.get(), _param_indi_inertia_y.get(), _param_indi_inertia_z.get());

	// 7. INDI 增量力矩核心公式: Δτ = J * (ν - Ω_dot_f)
	const matrix::Vector3f delta_torque = (virtual_accel - filtered_ang_accel).emult(inertia_diag);

	// 8. 合成总力矩: τ = τ_f + Δτ
	matrix::Vector3f torque_cmd = filtered_actuator_torque + delta_torque;

	// 9. 抗积分/增量饱和限幅 (Anti-Windup Clamping)
	const float max_torque = _param_indi_max_torque.get();
	for (int i = 0; i < 3; ++i) {
		if (std::isnan(torque_cmd(i)) || std::isinf(torque_cmd(i))) {
			torque_cmd(i) = 0.0f;
		}
		torque_cmd(i) = matrix::constrain(torque_cmd(i), -max_torque, max_torque);
	}

	// 记录上一拍输出
	_last_torque_cmd = torque_cmd;

	// 10. 发布至 uORB vehicle_torque_setpoint
	vehicle_torque_setpoint_s torque_setpoint{};
	torque_setpoint.timestamp = hrt_absolute_time();
	torque_setpoint.timestamp_sample = ang_vel_msg.timestamp;
	torque_setpoint.xyz[0] = torque_cmd(0);
	torque_setpoint.xyz[1] = torque_cmd(1);
	torque_setpoint.xyz[2] = torque_cmd(2);

	_vehicle_torque_setpoint_pub.publish(torque_setpoint);
}

} // namespace control
} // namespace px4
