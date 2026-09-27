#pragma once

#include "SecondOrderButterworthFilter.hpp"
#include <matrix/matrix/math.hpp>
#include <uORB/Publication.hpp>
#include <uORB/Subscription.hpp>
#include <uORB/topics/vehicle_angular_velocity.h>
#include <uORB/topics/vehicle_rates_setpoint.h>
#include <uORB/topics/vehicle_torque_setpoint.h>
#include <uORB/topics/vehicle_control_mode.h>
#include <uORB/topics/parameter_update.h>
#include <px4_platform_common/module_params.h>
#include <px4_platform_common/px4_work_queue/ScheduledWorkItem.hpp>

namespace px4
{
namespace control
{

/**
 * @brief PX4 增量非线性动态逆 (INDI) 姿态角速度控制器核心类
 */
class RateControlINDI : public ModuleParams, public px4::ScheduledWorkItem
{
public:
	RateControlINDI();
	~RateControlINDI() override;

	/** @brief 模块初始化与 uORB 回调绑定 */
	bool init();

	/** @brief 周期性主控制循环 (由 IMU 数据更新唤醒) */
	void Run() override;

private:
	/** @brief 参数更新处理 */
	void update_params();

	/** @brief 执行 INDI 核心算法并输出力矩 */
	void compute_indi_torque(float dt);

	// uORB 订阅者
	uORB::SubscriptionCallbackWorkItem _vehicle_angular_velocity_sub{this, ORB_ID(vehicle_angular_velocity)};
	uORB::Subscription _vehicle_rates_setpoint_sub{ORB_ID(vehicle_rates_setpoint)};
	uORB::Subscription _vehicle_control_mode_sub{ORB_ID(vehicle_control_mode)};
	uORB::Subscription _parameter_update_sub{ORB_ID(parameter_update)};

	// uORB 发布者
	uORB::Publication<vehicle_torque_setpoint_s> _vehicle_torque_setpoint_pub{ORB_ID(vehicle_torque_setpoint)};

	// 滤波器实例
	SecondOrderButterworthFilter3D _ang_accel_filter;  ///< 传感器角加速度滤波器
	SecondOrderButterworthFilter3D _actuator_filter;   ///< 执行器指令对称延迟匹配滤波器

	// 状态记忆变量
	matrix::Vector3f _last_angular_velocity{0.0f, 0.0f, 0.0f};
	matrix::Vector3f _last_torque_cmd{0.0f, 0.0f, 0.0f};
	uint64_t _last_run_timestamp{0};
	bool _is_active{false};

	// PX4 参数定义
	DEFINE_PARAMETERS(
		(ParamBool<px4::params::INDI_ENABLE>) _param_indi_enable,
		(ParamFloat<px4::params::INDI_RATE_P_X>) _param_indi_rate_p_x,
		(ParamFloat<px4::params::INDI_RATE_P_Y>) _param_indi_rate_p_y,
		(ParamFloat<px4::params::INDI_RATE_P_Z>) _param_indi_rate_p_z,
		(ParamFloat<px4::params::INDI_FILT_CUTOFF>) _param_indi_filt_cutoff,
		(ParamFloat<px4::params::INDI_INERTIA_X>) _param_indi_inertia_x,
		(ParamFloat<px4::params::INDI_INERTIA_Y>) _param_indi_inertia_y,
		(ParamFloat<px4::params::INDI_INERTIA_Z>) _param_indi_inertia_z,
		(ParamFloat<px4::params::INDI_MAX_TORQUE>) _param_indi_max_torque
	)
};

} // namespace control
} // namespace px4
