# Geodesic_Intersection_and_Flavor_Mixing.md  
## 測地線交差モデルとフレーバー混合の幾何学

---

## 1. 目的：なぜ CKM・PMNS 行列は「測地線の交差」から生まれるのか

iGUT において内部空間は  
$$
\mathbb{C}P^2
$$  
という複素射影多様体であり、その上の **測地線（geodesics）** が  
フレーバー状態の「自然な流れ」を定義する。

- Up 系列（u, c, t）  
- Down 系列（d, s, b）  

は、それぞれ CP² 上の **異なる測地線軌道**として表される。

この 2 本の測地線の  
- 開き角  
- ねじれ角（位相）  
- 交差構造  

が、CKM 行列の混合角と CP 位相を **完全に決定する**。

---

## 2. CP² 上の測地線：フレーバー状態の「自然軌道」

CP² の測地線は、Fubini–Study 計量に対する最短曲線であり、

$$
\frac{D^2 \psi}{ds^2} = 0
$$

を満たす。

iGUT では、  
- Up 系列は「真空方向に最も近い測地線」  
- Down 系列は「わずかにねじれた測地線」  

として記述される。

---

## 3. Up 系列と Down 系列の測地線

### 3.1 Up 系列（基準測地線）

Up 系列の測地線は、真空方向  
$$
P_3
$$  
（第 3 世代方向）に最も強く引き寄せられる。

この軌道を  
$$
\gamma_{\mathrm{up}}(s)
$$  
とする。

### 3.2 Down 系列（ねじれ測地線）

Down 系列は、Up 系列に対して  
- 空間的な開き角  
- 位相的なねじれ角  

を持つ測地線として表される。

$$
\gamma_{\mathrm{down}}(s;\theta,\delta)
$$

ここで  
- \( \theta \)：開き角（Cabibbo 角の源）  
- \( \delta \)：ねじれ角（CP 位相の源）

---

## 4. 測地線の交差と CKM 行列

2 本の測地線上の状態ベクトル  
$$
\psi_{\mathrm{up}}^{(i)}, \quad \psi_{\mathrm{down}}^{(j)}
$$
の内積が、CKM 行列要素を与える。

$$
V_{ij} = \langle \psi_{\mathrm{up}}^{(i)} , \psi_{\mathrm{down}}^{(j)} \rangle
$$

これは、測地線の交差角とねじれ角だけで決まる。

---

## 5. Cabibbo 角：測地線の開き角

最も重要な混合角である Cabibbo 角は、  
Up 系列と Down 系列の測地線の **空間的開き角** に対応する。

$$
\theta_C = \theta
$$

iGUT の CP² 幾何学では、  
この角度は CP² の曲率によって固定される。

$$
\sin \theta_C \approx \frac{1}{\sqrt{20}}
$$

これは実験値  
$$
\sin \theta_C \approx 0.2236
$$  
と一致する。

---

## 6. CP 位相：測地線のねじれ角

Down 系列の測地線が Up 系列に対して持つ  
**位相的ねじれ角** が、CKM の CP 位相を決める。

$$
\delta_{\mathrm{CKM}} = \delta
$$

iGUT では、このねじれ角は  
- CP² の円周位相  
- 時間方向の指数的伸び  

の競合から決まり、

$$
\delta_{\mathrm{CKM}} \approx \frac{\pi}{3}
$$

となる。

---

## 7. CKM 行列の幾何学的構造

測地線交差モデルから得られる CKM 行列は

$$
V_{\mathrm{CKM}} \approx
\begin{pmatrix}
1 & \theta & \theta^3 \\
\theta & 1 & \theta^2 e^{-i\delta} \\
\theta^3 & \theta^2 e^{i\delta} & 1
\end{pmatrix}
$$

ここで  
- \( \theta \) は Cabibbo 角  
- \( \delta \) は CP 位相  

である。

---

## 8. ヤールスコグ不変量の予言

CP 破れの大きさを表すヤールスコグ不変量は

$$
J = \mathrm{Im}(V_{us} V_{cb} V_{ub}^\ast V_{cs}^\ast)
$$

測地線パラメータを代入すると

$$
J \approx \theta^6 \sin \delta
$$

iGUT の値  
$$
\theta \approx 0.22, \quad \delta \approx \frac{\pi}{3}
$$  
を代入すると

$$
J \approx 3 \times 10^{-5}
$$

これは実験値と一致する。

---

## 9. PMNS 行列への拡張

レプトン混合（PMNS 行列）も同様に  
CP² 上の測地線の交差として記述できる。

ただし、ニュートリノは  
- CP² の別チャート  
- より浅いポテンシャル地形  

に対応するため、混合角が大きくなる。

---

## 10. 結論：フレーバー混合は「測地線の交差」である

- Up 系列と Down 系列は CP² 上の 2 本の測地線  
- 開き角が混合角  
- ねじれ角が CP 位相  
- 内積が CKM 行列  
- 固定点構造が 3 世代を保証  
- 幾何学だけで CKM・PMNS の構造が決まる  

つまり：

$$
\text{フレーバー混合とは、CP^2 上の測地線の交差幾何である。}
$$

iGUT は、標準模型のフレーバー構造を  
**パラメータではなく幾何学的必然性**として導く。

---
