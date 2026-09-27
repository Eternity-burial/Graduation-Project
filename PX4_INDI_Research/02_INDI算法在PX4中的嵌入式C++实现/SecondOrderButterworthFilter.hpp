#pragma once

#include <matrix/matrix/math.hpp>
#include <cmath>

namespace px4
{
namespace control
{

/**
 * @brief 高性能离散二阶巴特沃斯低通数字滤波器 (支持 3D 向量 matrix::Vector3f)
 * 采用双线性变换法 (Tustin with frequency pre-warping) 实现精确截止频率设计
 */
class SecondOrderButterworthFilter3D
{
public:
	SecondOrderButterworthFilter3D() = default;
	~SecondOrderButterworthFilter3D() = default;

	/**
	 * @brief 初始化或重新配置滤波器参数
	 * @param sample_freq 采样频率 (Hz), 例如 500.0f
	 * @param cutoff_freq 截止频率 (Hz), 例如 35.0f
	 */
	void set_cutoff_frequency(float sample_freq, float cutoff_freq)
	{
		if (sample_freq <= 0.0f || cutoff_freq <= 0.0f || cutoff_freq >= sample_freq * 0.5f) {
			// 保护：若频率不合法，设为直通滤波
			_b0 = 1.0f; _b1 = 0.0f; _b2 = 0.0f;
			_a1 = 0.0f; _a2 = 0.0f;
			return;
		}

		_sample_freq = sample_freq;
		_cutoff_freq = cutoff_freq;

		// 预畸变修正 (Pre-warping)
		const float pi = 3.14159265358979323846f;
		const float wa = 2.0f * sample_freq * std::tan(pi * cutoff_freq / sample_freq);
		const float wa2 = wa * wa;
		const float sqrt2_wa = std::sqrt(2.0f) * wa;
		const float sample_freq2 = 4.0f * sample_freq * sample_freq;

		const float denom = sample_freq2 + 2.0f * sqrt2_wa * sample_freq + wa2;

		_b0 = wa2 / denom;
		_b1 = 2.0f * _b0;
		_b2 = _b0;

		_a1 = (2.0f * wa2 - 2.0f * sample_freq2) / denom;
		_a2 = (sample_freq2 - 2.0f * sqrt2_wa * sample_freq + wa2) / denom;

		reset();
	}

	/**
	 * @brief 重置滤波器内部历史状态
	 */
	void reset(const matrix::Vector3f &initial_val = matrix::Vector3f(0.0f, 0.0f, 0.0f))
	{
		_x1 = initial_val;
		_x2 = initial_val;
		_y1 = initial_val;
		_y2 = initial_val;
		_initialized = true;
	}

	/**
	 * @brief 输入当前时刻原始值，计算输出滤波值
	 * @param raw 当前采样值 x(k)
	 * @return 滤波后的输出值 y(k)
	 */
	matrix::Vector3f update(const matrix::Vector3f &raw)
	{
		if (!_initialized) {
			reset(raw);
			return raw;
		}

		// 差分方程: y(k) = b0*x(k) + b1*x(k-1) + b2*x(k-2) - a1*y(k-1) - a2*y(k-2)
		matrix::Vector3f filtered = raw * _b0 + _x1 * _b1 + _x2 * _b2 - _y1 * _a1 - _y2 * _a2;

		// 更新历史状态
		_x2 = _x1;
		_x1 = raw;
		_y2 = _y1;
		_y1 = filtered;

		return filtered;
	}

	/**
	 * @brief 获取当前最新的滤波值
	 */
	matrix::Vector3f get_current_value() const { return _y1; }

private:
	float _sample_freq{500.0f};
	float _cutoff_freq{35.0f};

	float _b0{1.0f};
	float _b1{0.0f};
	float _b2{0.0f};
	float _a1{0.0f};
	float _a2{0.0f};

	matrix::Vector3f _x1{0.0f, 0.0f, 0.0f};
	matrix::Vector3f _x2{0.0f, 0.0f, 0.0f};
	matrix::Vector3f _y1{0.0f, 0.0f, 0.0f};
	matrix::Vector3f _y2{0.0f, 0.0f, 0.0f};

	bool _initialized{false};
};

} // namespace control
} // namespace px4
