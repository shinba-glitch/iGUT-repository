import numpy as np

# ==========================================
# 1. 質量キャリブレーションで得られた確定パラメータ
# ==========================================
# 普遍的エッジ・テンション (OS Geometry)
A = 0.887232
C = 11941.536563

# アップ系列 自己エネルギー
alpha_u = 0.443615
beta_u  = 0.121900
gamma_u = 1.000000

# ダウン系列 自己エネルギー
alpha_d = 0.442553
beta_d  = 0.000100
gamma_d = 5129.916649

# ==========================================
# 2. 3世代ヘッシアンの対角成分（質量の2乗）
# ==========================================
m_u2 = A - 2*alpha_u
m_c2 = A - 2*beta_u
m_t2 = C - 2*gamma_u

m_d2 = A - 2*alpha_d
m_s2 = A - 2*beta_d
m_b2 = C - 2*gamma_d

# ==========================================
# 3. 有効 2x2 混合ブロックの構築と対角化
# ==========================================
# オフダイアゴナル成分を生成する幾何学的結合係数 k (仮定)
# ※ 幾何学的な交差項の強さを表すオーダー1のパラメータ
k = 0.5 

# K行列要素 (1-3世代、2-3世代の幾何学的テンション結合)
# 最も素朴にエッジテンションの幾何平均に比例すると仮定
K13 = k * np.sqrt(A * C)
K23 = k * np.sqrt(A * C)

# 第3世代を積分消去して生じる有効オフダイアゴナル項 epsilon
eps_u = (K13 * K23) / m_t2
eps_d = (K13 * K23) / m_b2

print(f"【Effective 1-2 Mixing Terms (epsilon)】")
print(f" eps_u = {eps_u:.6f}")
print(f" eps_d = {eps_d:.6f}\n")

# 対角化角 theta の計算 (tan(2*theta) = 2*eps / (m2^2 - m1^2))
tan_2theta_u = 2 * eps_u / (m_c2 - m_u2)
theta_u = 0.5 * np.arctan(tan_2theta_u)

tan_2theta_d = 2 * eps_d / (m_s2 - m_d2)
theta_d = 0.5 * np.arctan(tan_2theta_d)

# ==========================================
# 4. カビボ角の抽出
# ==========================================
# CKM (1,2) 成分の幾何学的角度
theta_C_rad = abs(theta_d - theta_u)
theta_C_deg = np.degrees(theta_C_rad)

print(f"【Geometric Cabibbo Angle Calculation】")
print(f" theta_u (Up sector rotation)   = {np.degrees(theta_u):.4f} degrees")
print(f" theta_d (Down sector rotation) = {np.degrees(theta_d):.4f} degrees")
print(f"----------------------------------------")
print(f" theta_C = |theta_d - theta_u|  = {theta_C_deg:.4f} degrees")
print(f" (Experimental Target: ~ 13.0 degrees)")
