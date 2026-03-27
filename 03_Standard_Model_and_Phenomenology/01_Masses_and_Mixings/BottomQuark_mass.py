import numpy as np
from scipy.optimize import minimize

# 1. アップ系列で得られた OS 幾何パラメータ（あなたの実行結果をここに貼る）
A_fixed = 0.887232      # 例：アップ系列の最適化結果
C_fixed = 11941.536563  # 例：アップ系列の最適化結果

# 2. ダウン系列のターゲット質量 (MeV)
m_d_target = 4.7
m_s_target = 96.0
m_b_target = 4180.0

m_d2_target = m_d_target**2
m_s2_target = m_s_target**2
m_b2_target = m_b_target**2

# トップのときと同様に、b を基準にした比を使う
ratio_dt = m_d2_target / m_b2_target
ratio_st = m_s2_target / m_b2_target

print(f"[Down sector target ratios]")
print(f" d/b ratio: {ratio_dt:.2e}")
print(f" s/b ratio: {ratio_st:.2e}")

# 3. 損失関数： (alpha_d, beta_d, gamma_d) だけを動かす
def loss_down(params):
    alpha_d, beta_d, gamma_d = params

    # 質量公式（アップ系列と同じ構造を流用）
    m_d2 = A_fixed - 2*alpha_d
    m_s2 = A_fixed - 2*beta_d
    m_b2 = C_fixed - 2*gamma_d

    # 物理性チェック
    if m_d2 <= 0 or m_s2 <= 0 or m_b2 <= 0:
        return 1e10

    r_db = m_d2 / m_b2
    r_sb = m_s2 / m_b2

    return (np.log(r_db) - np.log(ratio_dt))**2 + (np.log(r_sb) - np.log(ratio_st))**2

# 4. 最適化の実行
initial_guess = [0.4, 0.3, 1000.0]  # 適当な初期値
bounds = [(0.0001, None), (0.0001, None), (0.0001, None)]

result = minimize(loss_down, initial_guess, bounds=bounds, method='Nelder-Mead')

alpha_d_opt, beta_d_opt, gamma_d_opt = result.x

print("\n[Optimized Down-sector self-energies]")
print(f" alpha_d = {alpha_d_opt:.6f}")
print(f" beta_d  = {beta_d_opt:.6f}")
print(f" gamma_d = {gamma_d_opt:.6f}")

# 5. 再現された質量をチェック
m_b2_model = C_fixed - 2*gamma_d_opt
m_d_reproduced = np.sqrt((A_fixed - 2*alpha_d_opt) / m_b2_model) * m_b_target
m_s_reproduced = np.sqrt((A_fixed - 2*beta_d_opt) / m_b2_model) * m_b_target

print("\n[Reproduced Down-sector masses (normalized to b = 4180 MeV)]")
print(f" m_d = {m_d_reproduced:.2f} MeV (Target: {m_d_target} MeV)")
print(f" m_s = {m_s_reproduced:.2f} MeV (Target: {m_s_target} MeV)")
print(f" m_b = {m_b_target:.2f} MeV (Target: {m_b_target} MeV)")
