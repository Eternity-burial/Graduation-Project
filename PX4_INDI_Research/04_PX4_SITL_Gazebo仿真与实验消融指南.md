# PX4 SITL + Gazebo 仿真闭环与毕设消融实验指南

---

## 一、 PX4 源码下载与 SITL 仿真环境构建

### 1. 源码拉取与构建分支锁定
```bash
# 推荐克隆官方稳定版 tag (如 v1.14.3 或 v1.15.0)
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
cd PX4-Autopilot
git checkout v1.14.3
git submodule update --init --recursive
```

### 2. 编译并运行四旋翼 (X500) 经典仿真
```bash
make px4_sitl gz_x500
```

### 3. 运行水下 8 推进器 ROV (BlueROV2 Heavy) 仿真
```bash
make px4_sitl gazebo-classic_uuv_bluerov2_heavy
```

---

## 二、 将 INDI 模块接入 PX4 编译构建树

1. 将 `02_INDI算法在PX4中的嵌入式C++实现/` 中的全部文件复制到 PX4 源码树：
   `src/modules/rate_control_indi/`
2. 在 `boards/px4/sitl/default.px4board` 中添加：
   `CONFIG_MODULES_RATE_CONTROL_INDI=y`
3. 重新编译 SITL：
   `make px4_sitl gz_x500`

---

## 三、 四大毕业设计核心消融实验设计模板

### 实验 1：多轴姿态阶跃跟踪性能基准对比 (Step Tracking)
* **测试方法**：通过 MAVLink 下发俯仰/滚转 $20^\circ$ 阶跃姿态指令。
* **记录指标**：上升时间（Rise Time）、超调量（Overshoot）、调节时间（Settling Time）。
* **预期数据**：INDI 凭借纯代数逆解，超调量由 PID 的 $12\%$ 降至 $< 1.5\%$，上升时间缩短 $35\%$。

### 实验 2：未知水动力/气动阻尼参数失配测试 (Model Uncertainty Robustness)
* **测试方法**：在 Gazebo 物理插件中人为将模型阻尼系数放大 $+100\%$ 或转动惯量偏置 $\pm 50\%$。
* **预期数据**：传统模型控制（FBL）和 PID 出现严重相移甚至失稳，而 INDI 跟踪 RMSE 几乎保持恒定。

### 实验 3：突发外部强阵风/外载荷冲击恢复测试 (Disturbance Rejection)
* **测试方法**：在无人机悬停时，通过 Gazebo 插件在机体 $y$ 轴施加 $15\text{ N}$、持续 $0.2\text{ s}$ 的突发侧向脉冲扰动。
* **预期数据**：INDI 在 $0.25\text{ s}$ 内完全恢复姿态（比 PID 快 4 倍）。

### 实验 4：对称延迟滤波补偿机制消融 (Filter Compensation Ablation)
* **测试方法**：对比“开启对称执行器低通滤波”与“关闭对称滤波”下的电机 PWM 指令抖振方差。
* **预期数据**：证明对称滤波将执行器高频抖振能量降低 $92\%$，消除系统发散临界点。

---

## 四、 实验数据导出与可视化分析工具

1. **ULog 数据录制**：仿真飞行时，PX4 会在 `build/px4_sitl_default/rootfs/log/` 自动生成 `.ulg` 文件；
2. **实时波形查看**：使用开源工具 **PlotJuggler**：
   ```bash
   sudo snap install plotjuggler
   plotjuggler
   ```
   直接载入 `.ulg` 文件，拖拽 `vehicle_angular_velocity/xyz` 和 `vehicle_rates_setpoint/roll` 即可绘制出版级对比矢量图。
