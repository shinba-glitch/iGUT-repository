# 27. Strong CP Problem and $\mathbb{C}P^2$ Holonomy
（強いCP問題と $\mathbb{C}P^2$ ホロノミー：幾何学的な $\theta$ 真空の相殺）

**【位置づけ】**
本章では、標準模型（SM）において未解決である「強いCP問題（Strong CP Problem）」に対し、未知の素粒子（アクシオン）を導入することなく、純粋な代数幾何学的な解答を与える。
具体的には、外部時空のトポロジーに由来する $\theta _{\text{QCD}}$ 項がスペクトル作用の対称性によって消失すること、および内部空間 $\mathbb{C}P^2 \times \mathbb{H}$ の四元数構造によってクォーク質量行列の行列式の位相 $\arg\det M _{q}$ が厳密にゼロに固定されることを、具体的な行列表現とアノマリーのシフト式を用いて証明する。

---

## 27.1 The Origin of the $\theta$-Term in the Spectral Action
（スペクトル作用における $\theta$ 項の起源と消失）

強い相互作用（QCD）のセクターにおいて、CP対称性を破る可能性のある物理的な実効位相 $\bar{\theta}$ は、以下の2つの項の和として定義される。

$$
\bar{\theta} = \theta _{\text{QCD}} + \arg\det M _{q}
$$

第一項の $\theta _{\text{QCD}}$ は、外部時空 $M^4$ 上の $SU(3)$ ゲージ束のトポロジー（第2チェルン数）に由来する位相である。
非可換幾何学のスペクトル作用 $S = \text{Tr}(f(D / \Lambda))$ の熱核展開において、パリティを破るトポロジカル項 $F \wedge F$ を出力する $a _{4}$ 係数は、一般に以下の構造を持つ。

$$
a _{4}(D^2) \supset \int _{M^4} \text{Tr} _{\mathcal{H} _{\text{internal}}}(\gamma _{5}^{\text{internal}}) \text{Tr} _{\text{color}}(F \wedge F)
$$

すなわち、外部時空に $\theta _{\text{QCD}}$ 項が現れるためには、内部ヒルベルト空間 $\mathcal{H} _{\text{internal}}$ におけるカイラリティ演算子 $\gamma _{5}^{\text{internal}}$ のトレースが非ゼロでなければならない。
しかし、iGUTにおいてカラー対称性 $SU(3)$ は、内部空間 $\mathbb{C}P^2$ 全体（バルク）の等長変換群（Isometry group）として定義されている。このような対称空間全体にわたる完全な等長変換のもとでは、内部カイラリティのトレースは厳密に消失する。

$$
\text{Tr} _{\mathcal{H} _{\text{internal}}}(\gamma _{5}^{\text{internal}}) = 0
$$

したがって、iGUTの基本構造において、外部時空から生じる裸の真空角は基礎理論のレベルで幾何学的に完全に消失する。

$$
\theta _{\text{QCD}} = 0
$$

## 27.2 Explicit Calculation: Quaternionic Structure and Real Determinant
（明示的計算：四元数構造と実数行列式）

次に、第二項である質量行列の行列式の位相 $\arg\det M _{q}$ について、有限ディラック演算子 $D _{F}$ の2世代モデルを用いて計算する。
内部空間の質量行列 $M$ は、四元数体 $\mathbb{H}$ 上の $2 \times 2$ エルミート行列である。

$$
M = 
\begin{pmatrix}
m _{1} & q \\
q^\dagger & m _{2}
\end{pmatrix}
$$

ここで $m _{1}, m _{2}$ は実数の自己エネルギー、 $q = \alpha + \beta j$ （ $\alpha, \beta \in \mathbb{C}$ ）は四元数のエッジテンションである。
標準模型の複素ヒルベルト空間における作用を評価するため、これを複素表現 $\mathbb{H} \hookrightarrow M _{2}(\mathbb{C})$ に埋め込むと、以下の $4 \times 4$ 複素エルミート行列 $M _{\mathbb{C}}$ が得られる。

$$
M _{\mathbb{C}} = 
\begin{pmatrix}
m _{1} & 0 & \alpha & \beta \\
0 & m _{1} & -\bar{\beta} & \bar{\alpha} \\
\bar{\alpha} & -\beta & m _{2} & 0 \\
\bar{\beta} & \alpha & 0 & m _{2}
\end{pmatrix}
$$

ブロック行列の公式を用いてこの行列式 $\det M _{\mathbb{C}}$ を計算すると、 $q q^\dagger = |\alpha|^2 + |\beta|^2$ より、以下の結果が得られる。

$$
\det M _{\mathbb{C}} = (m _{1} m _{2} - |\alpha|^2 - |\beta|^2)^2
$$

非対角成分 $\alpha, \beta$ にいかなる複素位相が含まれていようとも、行列式は厳密に正の実数となることが線形代数的に証明された。

$$
\arg\det M _{q} = 0
$$

## 27.3 Geodesic Holonomy and the Survival of CKM Phases
（測地線ホロノミーとCKM位相の残存）

前節で $\arg\det M _{q} = 0$ が証明されたが、弱い相互作用における CKM 行列の CP 破れ（Jarlskog 不変量 $\neq 0$）は、この四元数構造と完全に両立する。

行列 $M _{\mathbb{C}}$ を対角化するシンプレクティック変換 $U \in USp(4)$ の固有ベクトルには、元の $\alpha, \beta$ の複素位相が保持される。
iGUTにおいて、弱い力を担うレプトンやWボソンは $\mathbb{C}P^2$ 上の「1次元測地線」に局在している。忘却関手によって内部空間の対称性が破れる際、直交する方向（ $j, k$ に由来する $\beta$ 成分）の位相は、対角化行列の積 $V _{\text{CKM}} = U _{u}^\dagger U _{d}$ において相殺しきれず、物理的な CP 位相 $\delta _{\text{CKM}}$ として残存する。

すなわち、「行列式全体の大域的な位相はゼロに固定されたまま、個々の混合行列には局所的なCP破れの位相が宿る」という両立が実現される。

## 27.4 The Chiral Anomaly and the Strict Vanishing of $\bar{\theta}$
（カイラルアノマリーと $\bar{\theta}$ の厳密な消失）

実際のQCD真空において、クォークの $U(1) _{A}$ カイラル変換 $q \to e^{i\gamma _{5}\alpha} q$ を行うと、藤川の手法による積分測度のアノマリーが生じ、パラメータは以下のようにシフトする。

$$
\theta _{\text{QCD}} \to \theta _{\text{QCD}} + 2N _{f} \alpha
$$

$$
\arg\det M _{q} \to \arg\det M _{q} - 2N _{f} \alpha
$$

このシフトにより、通常は両者が混ざり合う。しかし iGUT では、セクション27.1と27.2で証明した通り、基礎理論のレベルで初めから以下が幾何学的・代数的に固定されている。

$$
\theta _{\text{QCD}} = 0, \quad \arg\det M _{q} = 0
$$

この両者が独立してゼロに固定されているため、いかなる $\alpha$ を選んでカイラル回転を行おうとも、その和である物理的観測量 $\bar{\theta}$ はアノマリーシフトに対して常に不変なゼロを保つ。

$$
\bar{\theta} _{\text{phys}} = (\theta _{\text{QCD}} + 2N _{f} \alpha) + (\arg\det M _{q} - 2N _{f} \alpha) = 0 + 0 = 0
$$

## 27.5 The Fate of the Axion: Rigid Zero and Geometric Consistency
（アクシオンの運命：剛体的なゼロと幾何学的無矛盾性）

結論として、iGUTにおいて $\bar{\theta}$ は、動力学的なポテンシャルの緩和（ペッチェイ・クイン機構）によってゼロに落ちるのではなく、四元数構造と $\mathbb{C}P^2$ の等長変換という幾何学の「壁」によって初めから剛体的にゼロに固定されている。

このため、 $\bar{\theta}$ を動的に相殺するための未知のスカラー場（アクシオン）を導入する必要は一切ない。
標準模型における「なぜ弱い力ではCPが破れ、強い力ではCPが保存されるのか」という最大の不条理は、**「1次元測地線のホロノミー」と「4次元バルクの等長変換」の幾何学的な差異**、および**「四元数行列表現における実数行列式」**という純粋な数理物理学の帰結として完全に解明された。
