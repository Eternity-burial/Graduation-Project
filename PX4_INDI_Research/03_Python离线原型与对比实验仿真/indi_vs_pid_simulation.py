# -*- coding: utf-8 -*-
"""
PX4 INDI vs Classic PID 离线仿真与对比实验验证
涵盖：
1. 阶跃设定值跟踪响应
2. 突发外界阶跃力矩扰动抑制 (模拟突发大风/水下湍流)
3. 延迟补偿消融对比 (未补偿 vs 对称滤波补偿)
"""

import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

class Plant1D:
    def __init__(self, J=0.03, d_lin=0.05, d_quad=0.08, tau_act=0.03):
        self.J = J
        self.d_lin = d_lin
        self.d_quad = d_quad
        self.tau_act = tau_act
        self.omega = 0.0
        self.torque_actual = 0.0
        
    def step(self, torque_cmd, torque_dist, dt, noise_std=0.05):
        self.torque_actual += (torque_cmd - self.torque_actual) * (dt / self.tau_act)
        damping = self.d_lin * self.omega + self.d_quad * self.omega * abs(self.omega)
        omega_dot = (self.torque_actual - damping + torque_dist) / self.J
        self.omega += omega_dot * dt
        measured_omega = self.omega + np.random.normal(0, noise_std)
        return self.omega, measured_omega, omega_dot

class ButterworthFilter2nd:
    def __init__(self, fs=500.0, fc=30.0):
        wa = 2.0 * fs * np.tan(np.pi * fc / fs)
        wa2 = wa * wa
        sqrt2_wa = np.sqrt(2.0) * wa
        fs2 = 4.0 * fs * fs
        denom = fs2 + 2.0 * sqrt2_wa * fs + wa2
        
        self.b0 = wa2 / denom
        self.b1 = 2.0 * self.b0
        self.b2 = self.b0
        self.a1 = (2.0 * wa2 - 2.0 * fs2) / denom
        self.a2 = (fs2 - 2.0 * sqrt2_wa * fs + wa2) / denom
        
        self.x1, self.x2 = 0.0, 0.0
        self.y1, self.y2 = 0.0, 0.0
        
    def update(self, x):
        y = self.b0 * x + self.b1 * self.x1 + self.b2 * self.x2 - self.a1 * self.y1 - self.a2 * self.y2
        self.x2 = self.x1
        self.x1 = x
        self.y2 = self.y1
        self.y1 = y
        return y

def run_simulation():
    dt = 0.002
    t_end = 6.0
    time = np.arange(0, t_end, dt)
    N = len(time)
    
    sp = np.zeros(N)
    sp[time >= 1.0] = 3.0
    
    dist = np.zeros(N)
    dist[time >= 4.0] = 1.5
    
    # 1. 经典 PID
    plant_pid = Plant1D()
    hist_omega_pid = np.zeros(N)
    hist_torque_pid = np.zeros(N)
    Kp_pid, Ki_pid, Kd_pid = 0.25, 0.6, 0.008
    int_err = 0.0
    prev_err = 0.0
    
    for k in range(N):
        omega_real, omega_meas, _ = plant_pid.step(hist_torque_pid[max(0, k-1)], dist[k], dt)
        hist_omega_pid[k] = omega_real
        err = sp[k] - omega_meas
        int_err += err * dt
        int_err = np.clip(int_err, -2.0, 2.0)
        d_err = (err - prev_err) / dt
        prev_err = err
        cmd = Kp_pid * err + Ki_pid * int_err + Kd_pid * d_err
        hist_torque_pid[k] = np.clip(cmd, -3.0, 3.0)
        
    # 2. 未补偿 INDI
    plant_indi_nodelay = Plant1D()
    hist_omega_indi_nodelay = np.zeros(N)
    hist_torque_indi_nodelay = np.zeros(N)
    filt_acc_raw = ButterworthFilter2nd(fs=500.0, fc=30.0)
    prev_omega_meas = 0.0
    Kp_indi = 15.0
    J_est = 0.03
    
    for k in range(N):
        omega_real, omega_meas, _ = plant_indi_nodelay.step(hist_torque_indi_nodelay[max(0, k-1)], dist[k], dt)
        hist_omega_indi_nodelay[k] = omega_real
        raw_acc = (omega_meas - prev_omega_meas) / dt
        prev_omega_meas = omega_meas
        filt_acc = filt_acc_raw.update(raw_acc)
        nu = Kp_indi * (sp[k] - omega_meas)
        delta_tau = J_est * (nu - filt_acc)
        cmd = hist_torque_indi_nodelay[max(0, k-1)] + delta_tau
        hist_torque_indi_nodelay[k] = np.clip(cmd, -3.0, 3.0)
        
    # 3. 对称延迟补偿 INDI
    plant_indi_prop = Plant1D()
    hist_omega_indi_prop = np.zeros(N)
    hist_torque_indi_prop = np.zeros(N)
    filt_acc_prop = ButterworthFilter2nd(fs=500.0, fc=30.0)
    filt_act_prop = ButterworthFilter2nd(fs=500.0, fc=30.0)
    prev_omega_meas = 0.0
    
    for k in range(N):
        omega_real, omega_meas, _ = plant_indi_prop.step(hist_torque_indi_prop[max(0, k-1)], dist[k], dt)
        hist_omega_indi_prop[k] = omega_real
        raw_acc = (omega_meas - prev_omega_meas) / dt
        prev_omega_meas = omega_meas
        filt_acc = filt_acc_prop.update(raw_acc)
        torque_f = filt_act_prop.update(hist_torque_indi_prop[max(0, k-1)])
        nu = Kp_indi * (sp[k] - omega_meas)
        delta_tau = J_est * (nu - filt_acc)
        cmd = torque_f + delta_tau
        hist_torque_indi_prop[k] = np.clip(cmd, -3.0, 3.0)
        
    # 绘图
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
    ax1.plot(time, sp, 'k--', label='目标参考 (Setpoint)', linewidth=1.5)
    ax1.plot(time, hist_omega_pid, 'g-', label='传统 PID 控制器', linewidth=1.5)
    ax1.plot(time, hist_omega_indi_nodelay, 'r:', label='未补偿 INDI (发散振荡)', alpha=0.7)
    ax1.plot(time, hist_omega_indi_prop, 'b-', label='提出之对称延迟补偿 INDI', linewidth=2.0)
    ax1.axvline(x=4.0, color='m', linestyle='--', alpha=0.7, label='突发力矩外扰 (+1.5 Nm)')
    ax1.set_ylabel('角速度 (rad/s)', fontsize=12)
    ax1.set_title('PX4 控制器性能基准对比：阶跃跟踪与突发扰动抑制', fontsize=14, fontweight='bold')
    ax1.grid(True, linestyle=':')
    ax1.legend(loc='upper left', fontsize=10)
    ax1.set_ylim(-1.0, 5.0)
    
    ax2.plot(time, hist_torque_pid, 'g-', label='PID 输出力矩', linewidth=1.2)
    ax2.plot(time, hist_torque_indi_prop, 'b-', label='INDI 对称补偿输出力矩', linewidth=1.5)
    ax2.set_xlabel('时间 (s)', fontsize=12)
    ax2.set_ylabel('控制力矩 (Nm)', fontsize=12)
    ax2.grid(True, linestyle=':')
    ax2.legend(loc='upper right', fontsize=10)
    
    plt.tight_layout()
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    plot_path = os.path.join(cur_dir, "indi_vs_pid_benchmark_result.png")
    plt.savefig(plot_path, dpi=300)
    print(f"Simulation plot saved successfully to: {plot_path}")
    plt.close()

if __name__ == '__main__':
    run_simulation()
