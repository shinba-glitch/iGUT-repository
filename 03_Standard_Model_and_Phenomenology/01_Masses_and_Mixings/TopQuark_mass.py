import numpy as np
from scipy.optimize import minimize

# 1. 現実のクォーク質量 (単位: MeV)
m_u_target = 2.2
m_c_target = 1270.0
m_t_target = 173000.0

# 質量の2乗
m_u2_target = m_u_target**2
m_c2_target = m_c_target**2
m_t2_target = m_t_target**2

# トップクォークに対する比率（2乗の比）
ratio_ut = m_u2_target / m_t2_target
ratio_ct = m_c2_target / m_t2_target

print(f"【Target Ratios】\n u/t ratio: {ratio_ut:.2e}\n c/t ratio: {ratio_ct:.2e}\n")

# 2. 損失関数（Loss Function）の定義
def loss(params):
    # gamma = 1.0 (基準スケール) として固定
    alpha, beta, A, C = params
    gamma = 1.0
    
    # 質量公式 (負の質量2乗は物理的でないため巨大なペナルティ)
    m_u2 = A - 2*alpha
    m_c2 = A - 2*beta
    m_t2 = C - 2*gamma
    
    if m_u2 <= 0 or m_c2 <= 0 or m_t2 <= 0:
        return 1e10
        
    # モデルの比率
    r_ut = m_u2 / m_t2
    r_ct = m_c2 / m_t2
    
    # 対数スケールでの誤差の2乗和 (桁違いの階層を評価するため)
    return (np.log(r_ut) - np.log(ratio_ut))**2 + (np.log(r_ct) - np.log(ratio_ct))**2

# 3. 最適化の実行
# 初期値 guess: [alpha, beta, A, C]
# C はトップ質量を出すために非常に大きく、A は比較的小さいと予想
initial_guess = [0.5, 0.1, 1.1, 10000.0]

# 制約: すべてのテンション・エネルギーは正 ( > 0.0001 )
bounds = [(0.0001, None), (0.0001, None), (0.0001, None), (0.0001, None)]

result = minimize(loss, initial_guess, bounds=bounds, method='Nelder-Mead')

# 4. 結果の出力
alpha_opt, beta_opt, A_opt, C_opt = result.x
gamma_opt = 1.0

print("【Optimized Parameters (OS Geometry)】")
print(f" alpha (Gen1 self-energy) = {alpha_opt:.6f}")
print(f" beta  (Gen2 self-energy) = {beta_opt:.6f}")
print(f" gamma (Gen3 self-energy) = {gamma_opt:.6f} (Fixed base scale)")
print(f" A     (Gen1-Gen2 tension)= {A_opt:.6f}")
print(f" C     (Gen1-Gen3 tension)= {C_opt:.6f}")

print("\n【Reproduced Mass Hierarchy (Normalized to Top = 173 GeV)】")
m_t2_model = C_opt - 2*gamma_opt
m_u_reproduced = np.sqrt((A_opt - 2*alpha_opt) / m_t2_model) * 173000
m_c_reproduced = np.sqrt((A_opt - 2*beta_opt) / m_t2_model) * 173000

print(f" m_u = {m_u_reproduced:.2f} MeV (Target: {m_u_target} MeV)")
print(f" m_c = {m_c_reproduced:.2f} MeV (Target: {m_c_target} MeV)")
print(f" m_t = 173000.00 MeV (Target: 173000.0 MeV)")
