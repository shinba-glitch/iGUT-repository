# 23b. The Unified Geodesic Equation: Wong Equations and the Semiclassical Bridge
（統合測地線方程式：ウォン方程式と半古典的架け橋）

**【位置づけ】**
第23章においてスペクトル作用の熱核展開から外部幾何学（アインシュタイン方程式）を導出した。
本章（23b章）では、確定した背景場（重力 $g_{\mu\nu}$ 、ゲージ場 $A_\mu^a$ 、ヒッグス場 $H$ ）の中を運動する古典的な「テスト粒子」のダイナミクスを記述する。
iGUT の OS アーキテクチャにおいて、これは Level 0〜2 の統合された接続に沿った「自由落下」の方程式であり、量子論的な「第24章：散乱振幅」へ向かうための経路積分の鞍点（半古典近似）として位置づけられる。

---

## 1. Unified Connection and the Principal of Parallel Transport（統合された接続と平行移動の原理）

iGUT の根本原理は、外部時空と内部空間を単一のディラック演算子 $D = D_M \otimes \mathbb{I} + \gamma_5 \otimes D_F$ で統合することにある。
この統合された幾何学に対応して、外部のレヴィ＝チヴィタ接続 $\nabla^M$ と内部のゲージ接続 $A$ は、Quillen の超接続（Superconnection） $\hat{\nabla}$ として一本化される。

$$
\hat{\nabla} = \nabla^M \oplus A
$$

統合空間を飛ぶ古典粒子の「自由落下」は、この統合された接続に対する共変微分がゼロになる条件、すなわち「平行移動（Parallel Transport）」として数学的にただ一行で定義される。

$$
\frac{\hat{D} \mathcal{V}}{d\tau} = 0
$$

ここで $\mathcal{V}$ は、外部時空の速度ベクトル $u^\mu$ と内部空間の状態ベクトル（カラーやアイソスピン） $|\chi\rangle$ を統合した一般化された速度ベクトルである。
この単一の方程式を、外部と内部の成分に分解することで、私たちが観測する物理法則が導出される。

## 2. Derivation from the Worldline Action Principle（世界線作用原理からの導出）

統合測地線方程式は、内部自由度を持つ粒子の経路積分における鞍点（Saddle Point）として、変分原理 $\delta S = 0$ から導出される。
超接続 $\mathbb{A}$ に沿って運動する粒子の世界線作用 $S$ は、以下のように構成される。

$$
S[x, \chi] = \int d\tau \left[ \frac{1}{2} g_{\mu\nu}(x) \dot{x}^\mu \dot{x}^\nu + \langle \chi | i \frac{D}{d\tau} | \chi \rangle + \langle \chi | A_\mu(x) \dot{x}^\mu | \chi \rangle \right]
$$

この作用は、通常の測地線作用（外部重力）に、内部状態 $|\chi\rangle$ の運動エネルギー項と、ゲージ場 $A_\mu$ との相互作用項（Bohm-Aharonov型）を加えたものである。
iGUT の文脈において、この作用はスペクトル作用 $S_{\text{spec}} = \mathrm{Tr}\, f(D/\Lambda)$ の「1粒子極限（世界線表現）」として厳密に定式化される。

## 3. Wong Equations: The External Geodesic Deviation（ウォン方程式：外部測地線からの偏差）

外部時空の座標 $x^\mu$ に対する変分 $\delta x^\mu = 0$ から得られる運動方程式は、通常の測地線方程式に非可換ローレンツ力が加わった形、すなわち古典的な「ウォン方程式（Wong's equations）」となる。

$$
\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\nu\rho} \frac{dx^\nu}{d\tau} \frac{dx^\rho}{d\tau} = \frac{1}{m} \langle \chi | F^{\mu}_{\;\;\nu} | \chi \rangle \frac{dx^\nu}{d\tau}
$$

* **左辺:** 外部時空のクリストッフェル記号 $\Gamma^\mu_{\nu\rho}$ による重力効果。
* **右辺:** 内部幾何のねじれであるゲージ曲率 $F^\mu_{\;\;\nu}$ が、内部状態 $|\chi\rangle$ の期待値を通じて及ぼすゲージ力。

粒子の軌道は重力だけで決まる測地線から、内部に持つカラーや弱アイソスピンに応じて「逸脱」する。この方程式は、一般相対性理論と標準模型のゲージ相互作用が、古典粒子のレベルで完全に一本化されていることを示している。

## 4. Internal Parallel Transport: The Dynamics of Charge（内部平行移動：電荷のダイナミクス）

内部状態 $|\chi\rangle$ に対する変分 $\delta \chi = 0$ から得られる方程式は、内部空間の自由度が外部のゲージ接続 $A_\mu$ に沿って共変的に保存される条件を与える。

$$
\frac{D \chi}{d\tau} = \frac{d\chi}{d\tau} + A_\mu \frac{dx^\mu}{d\tau} \chi = 0
$$

粒子の持つカラー荷やアイソスピン荷は、外部時空を移動するにつれて、ゲージ場 $A_\mu$ との相互作用によって内部空間で「回転」するが、その「大きさ」は保存される。
この電荷の平行移動と、前節の軌道の偏差（ウォン方程式）は、互いに共変的（Covariant）であり、単一の超接続の作用の停留点として完全に統合されている。

## 5. The Semiclassical Bridge and the Zero-Order Approximation（半古典的架け橋とゼロ次近似）

本章で提示された統合測地線方程式は、「古典的世界線」と「古典的な内部状態（接続上の回転）」として SM 粒子を扱っている。
SM は本来量子場理論（QFT）であるが、この古典的記述は、完全な量子論の経路積分 $\int \mathcal{D}x \mathcal{D}\chi e^{iS}$ に対する**鞍点近似（Saddle Point Approximation）**、または **WKB近似** として幾何学的に正当化される。

$$
\text{Quantum Amplitude} = e^{iS_{\text{classical}} / \hbar} \times (\text{Quantum Fluctuations})
$$

統合測地線方程式は、この $S_{\text{classical}}$ を決定する「ゼロ次近似」である。
次章の「第24章：散乱振幅」では、この古典的な軌跡（鞍点）の周りでの量子的なゆらぎ、すなわちオンシェルの S行列を幾何学的に評価するプロセスへと移行する。本章は、オフシェルの幾何（Ch 23）からオンシェルの量子振幅（Ch 24）へ向かうための、必須の半古典的架け橋である。
