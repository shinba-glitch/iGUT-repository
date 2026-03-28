# Action Principle with Up–Down Splitting  
（アップ・ダウン分裂セクターをもつ Freudenthal 行列式の作用原理）

本稿では、例外ジョルダン代数 $\mathcal{H}_3(\mathbb{O})$ における  
Freudenthal 行列式を、アップ型・ダウン型の 2 セクターに分裂させた上で、  
それぞれの質量行列 $M_u, M_d$ に対する作用原理として定式化する。

目的は：
- **(1)** アップ型・ダウン型それぞれに「三重シーソー方程式」が現れること  
- **(2)** それらが同一の統一ポテンシャルから来ていること  
を、明示的な変分方程式として書き下すことである。

---

## 1. 単一セクターの Freudenthal 行列式（復習）

単一の $\mathcal{H}_3(\mathbb{O})$ 元

$$
X =
\begin{pmatrix}
\lambda_1 & y_{12} & \bar{y}_{13} \\
\bar{y}_{12} & \lambda_2 & y_{23} \\
y_{13} & \bar{y}_{23} & \lambda_3
\end{pmatrix}
$$

に対し、Freudenthal 行列式は

$$
\det(X)
= \lambda_1 \lambda_2 \lambda_3- \lambda_1 \|y_{23}\|^2- \lambda_2 \|y_{13}\|^2- \lambda_3 \|y_{12}\|^2+ 2\,\mathrm{Re}(y_{12} y_{23} y_{13})
$$

で与えられる。

前章では、混合項を無視した近似での変分

$$
\frac{\partial}{\partial \lambda_i} \det(X) = 0
$$

から

$$
\lambda_j \lambda_k = \|y_{jk}\|^2
$$

という「三重シーソー方程式」が得られた。

---

## 2. Up–Down Splitting：2 つの行列 $X_u, X_d$

複素構造 $J$ による分裂により、  
アップ型・ダウン型の 2 つの行列

$$
X_u,\quad X_d \in \mathcal{H}_3(\mathbb{O})
$$

が定義される。

それぞれの成分を

$$
X_u \sim (\lambda^{(u)}_i,\ y^{(u)}_{jk}), \quad
X_d \sim (\lambda^{(d)}_i,\ y^{(d)}_{jk})
$$

と書く。

ここでの仮説は：
- $\lambda^{(u)}_i \propto 1/m^{(u)}_i$  
- $\lambda^{(d)}_i \propto 1/m^{(d)}_i$

であり、両者は同じ「逆質量固有値」の構造を共有するが、  
複素構造 $J$ の符号により、
$y^{(u)}_{jk}$ と $y^{(d)}_{jk}$ の虚部のねじれが異なる。

---

## 3. 全作用：2 セクターの Freudenthal 行列式の和

最も素朴で、かつ自然な全作用は

$$
S_{\text{total}}
= -\alpha_u \det(X_u) - \alpha_d \det(X_d)
$$

と書ける（符号は「極大化／極小化」の慣習に依存）。

ここで $\alpha_u, \alpha_d > 0$ は  
アップ型・ダウン型セクターの重み（あるいは有効結合定数）である。

**第一近似として**、アップ・ダウン間の直接結合項は入れず、  
CKM はあくまで「対角化回転のズレ」として後から現れるものとする。

---

## 4. 変分方程式：2 つの独立した三重シーソー

各セクターについて、固有値に関する変分をとる：

$$
\frac{\partial S_{\text{total}}}{\partial \lambda^{(u)}_i}
= -\alpha_u \frac{\partial}{\partial \lambda^{(u)}_i} \det(X_u) = 0
$$

$$
\frac{\partial S_{\text{total}}}{\partial \lambda^{(d)}_i}
= -\alpha_d \frac{\partial}{\partial \lambda^{(d)}_i} \det(X_d) = 0
$$

混合項を無視した近似では、それぞれ独立に

$$
\lambda^{(u)}_j \lambda^{(u)}_k = \|y^{(u)}_{jk}\|^2
$$

$$
\lambda^{(d)}_j \lambda^{(d)}_k = \|y^{(d)}_{jk}\|^2
$$

という **2 組の三重シーソー方程式** が得られる。

これが「Dual Seesaw Mechanism」の最も単純な形である。

---

## 5. CKM の源泉：2 つの極値問題の「ねじれの差分」

ここまでの構造から、次の物語が得られる：

1. $X_u, X_d$ は、それぞれ独立に  
   Freudenthal 行列式の極値条件を満たすように  
   $\lambda^{(u)}_i, y^{(u)}_{jk}$ および  
   $\lambda^{(d)}_i, y^{(d)}_{jk}$ を調整する。
2. しかし、両者は **同じ複素射影空間 $\mathbb{C}P^2$** 上で、  
   複素構造 $J$ の符号が反転した空間に住んでいるため、  
   虚部のねじれ（位相）の取り方が異なる。
3. その結果、2 つの質量行列を対角化する回転  
   $U_u, U_d$ が異なり、そのズレ
   
   $$
   V_{\text{CKM}} = U_u^\dagger U_d
   $$
   
   が、観測される CKM 行列として現れる。

---

## 6. 今後の拡張：結合項と CP 破れ

本稿では、最も単純な

$$
S_{\text{total}} = -\alpha_u \det(X_u) - \alpha_d \det(X_d)
$$

のみを考えたが、よりリッチな構造として

$$
S_{\text{int}} = -\beta\, \mathrm{Re}\,\mathcal{F}(X_u, X_d)
$$

のような「アップ・ダウン間の干渉項」を導入することもできる。

ここで $\mathcal{F}$ は、例えば
- $y^{(u)}_{12} y^{(d)}_{23} y^{(u)}_{13}$ のような混合三重積
- あるいは、2 つの Jarlskog 型不変量の積

などが候補となる。
このような干渉項は、**CP 破れの大きさや CKM の位相構造を微調整する役割** を担う可能性がある。

---

## 7. 結論：2 つの Freudenthal 行列式の極値としての Dual Seesaw

- アップ型・ダウン型セクターは、それぞれ独立に Freudenthal 行列式の極値条件を満たす。
- その結果として、2 組の三重シーソー方程式が現れ、各セクターの質量階層と混合強度を拘束する。
- 複素構造 $J$ の符号反転により、2 つの極値問題は「ねじれの位相空間」を異にし、そのズレが CKM 行列として観測される。

> **命題（構造レベル）：** > iGUT における CKM 行列は、アップ型・ダウン型の 2 つの Freudenthal 行列式の極値問題の「差分」として幾何学的に定義される。質量階層と混合角を同時に拘束する三重シーソー構造を生む。
