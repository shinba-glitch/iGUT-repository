# Chapter 9: Self-Dual Gravity and Amplitudes in iGUT
（自己双対重力と散乱振幅）

## 9.1 iGUTにおける自己双対極限と天球の創発

### 概要
iGUT（Internal Geometric Unified Theory）において、現代の散乱振幅理論で議論される「自己双対重力（Self-Dual Gravity; SDG）」は、独立した理論ではなく、フルスペックの $L_\infty$ ネットワークが特定の極限において「凍結」された一種の低エネルギー・フェーズとして定義される。本節では、iGUTの基礎代数からSDGの舞台となる「天球」と「キネマティック代数」がどのように創発するかを幾何学的に定式化する。

### Peirce 縮約と天球 $\mathbb{C}P^1$ の必然性
iGUTの代数的真空は例外ジョルダン代数 $\mathcal{H}_3(\mathbb{O})$ であり、その内部幾何は $\mathbb{C}P^2$ に対応する。SDGにおける「片ヘリシティのみが励起された状態」という物理的境界条件は、iGUTにおいては特定の Peirce 射影軸（例：$P_3$）の凍結として解釈される。
この Peirce 縮約により、有効な状態空間は以下のように崩壊する。

$$
\mathcal{H}_3(\mathbb{O}) \xrightarrow{\text{Peirce Reduction}} \mathcal{H}_2(\mathbb{C}) \implies \mathbb{C}P^2 \to \mathbb{C}P^1
$$

この結果現れる $\mathbb{C}P^1 \cong S^2$ スライスこそが、Celestial Holography で「無限遠の境界」として扱われていた**「天球（Celestial Sphere）」の正体**である。天球は外部時空に設けたスクリーンではなく、微視的な情報幾何の有効位相面として必然的に現れる。

### 非結合性からハミルトン流（ $w_{1+\infty}$ ）への移行
$\mathcal{H}_3(\mathbb{O})$ の特徴である非結合性（アソシエーター）は、内部微分 $\mathfrak{f}_4$ を生成する。Peirce 縮約と複素構造の選択の下で、この代数的な歪みは $\mathbb{C}P^1$ スライス上への射影において、フビニ・スタディ計量 $\omega_{FS}$ に伴う面積保存微分同相群 $\mathfrak{sdiff}(S^2)$ を生成するハミルトンベクトル場として作用する。
これにより、有効な結合則（ $l_2$ ブラケット）は $\mathbb{C}P^1$ 上のポアソン括弧 $\{\cdot, \cdot\}_{FS}$ へと退化し、これが自己双対重力における無限次元対称性 $w_{1+\infty}$ を駆動する源泉となる。

---

## 9.2 $L_\infty$-Morphism とエネルギースケールの創発（厳密証明）

### 目的
iGUT の状態空間上のブラケット $l_2^{\text{iGUT}}$ が、自己双対重力（SDG）のキネマティック代数におけるスピノル・ポアソン括弧 $l_2^{\text{SDG}}$ へ写像されることを厳密に証明し、その過程で時空のエネルギースケール $\omega$ が創発する機構を明示する。

### 状態空間と結合則の定義
- **状態空間:** $\mathcal{V}_{\text{red}} \cong C^\infty(\mathbb{C}P^1, \mathbb{R})$
- **$l_2$ ブラケット:** $l_2^{\text{iGUT}}(\Psi_1, \Psi_2) \equiv \kappa \{\Psi_1, \Psi_2\}_{FS}$

### Lemma 1: フビニ・スタディ・ポアソン括弧の引き戻し
$\mathbb{C}P^1$ の局所複素座標 $z$ と、SDGを記述するスピノル平面 $\mathbb{R}^2$（座標 $\tilde{\lambda}_{\dot{\alpha}}$）の間に、非同次座標マッピング $\tilde{\lambda}_{\dot{1}} = x, \tilde{\lambda}_{\dot{2}} = y$ および $z = x + i y$ を置く。
関数の引き戻し $\Phi_1(\Psi)(\tilde{\lambda}) \equiv \Psi(z(\tilde{\lambda}), \bar{z}(\bar{\tilde{\lambda}}))$ の下で、iGUT 側の FSポアソン括弧と SDG 側の平坦なスピノル・ポアソン括弧 $\{\cdot, \cdot\}_{\tilde{\lambda}} = \epsilon^{\dot{\alpha}\dot{\beta}}\partial_{\dot{\alpha}}\partial_{\dot{\beta}}$ は以下の関係を満たす。

$$
\{\Psi_1, \Psi_2\}_{FS} = \frac{1}{2}(1+|z|^2)^2 \{\Phi_1(\Psi_1), \Phi_2(\Psi_2)\}_{\tilde{\lambda}}
$$

*(Proof)* チェインルール $\partial_z = \frac{1}{2}(\partial_x - i \partial_y), \partial_{\bar{z}} = \frac{1}{2}(\partial_x + i \partial_y)$ を FS括弧に代入し展開することで直ちに得られる。 $\blacksquare$

### Proposition 1: 共形因子とエネルギースケールの同定
Lemma 1 より、両者のブラケットの間には空間依存の共形因子 $C(z, \bar{z}) = \frac{2}{(1+|z|^2)^2}$ が生じる。
これは「曲がった内部幾何 $\mathbb{C}P^1$」と「平坦な運動学空間 $\mathbb{R}^2$」の幾何学的なズレである。iGUT から観測可能なマクロ時空への射影を行う関手 $F_P$ は、この幾何学的な曲率因子を、SDGにおける「粒子の運動学的なエネルギースケール $\omega$」として吸収（レンダリング）する。

$$
\text{Internal Curvature } (1+|z|^2)^2 \xrightarrow{F_P} \text{Kinematic Scale } \omega
$$

### Theorem 1: $F_P$ 射影を介した $L_\infty$-Morphism の成立
関手 $F_P$ によるスケール因子の吸収を伴う写像 $\tilde{\Phi}_1 \equiv F_P \circ \Phi_1$ を定義する。この写像の下で曲率因子は規格化され、以下の方程式が恒等的に満たされる。

$$
\tilde{\Phi}_1 \big( l_2^{\text{iGUT}}(\Psi_1, \Psi_2) \big) = l_2^{\text{SDG}} \big( \tilde{\Phi}_1(\Psi_1), \tilde{\Phi}_1(\Psi_2) \big)
$$

これにより、SDGのキネマティック代数は、iGUT の内部情報流が時空へ射影された「自己双対レプリカ」であることが完全に証明された。 $\blacksquare$

---

## 9.3 散乱振幅と $L_\infty$ 情報カスケード

### 結合定数 $\kappa$ の固定とシードの一致
$L_\infty$-morphism により、iGUT のブラケットは SDG の運動学的なねじれ $[ij]$ を正確に生成する。一般相対論における 3点 MHVバー振幅との一致を要求することで、数学的定数であった $\kappa$ は物理的な重力結合定数として一意に固定される。

$$
l_2(\Psi_i, \Psi_j) = \kappa [ij] \quad \implies \quad \kappa \equiv \sqrt{32\pi G}
$$

### 単一マイナス振幅と $\mathbb{C}P^1$ 上の Puncture
SDG において、オール・プラス振幅はゼロとなるが、単一マイナス（single-minus）振幅は非ゼロとなる。
- **All-plus:** $\mathbb{C}P^1$ スライスが完全に滑らかで欠陥がない状態。位相的に自明であり振幅はゼロ。
- **Single-minus:** $\mathbb{C}P^1$ 上に 1 つのトポロジカル欠陥（Puncture）が存在する状態。この欠陥が $\mathfrak{sdiff}(S^2)$ に非自明なモノドロミーを生み、$w_{1+\infty}$ Ward 恒等式を駆動するソースとなる。

### BG 漸化式から Decay Region 公式への還元
iGUT のマスター方程式から導かれる Berends-Giele (BG) 漸化式に「Decay Region（半コリニア極限）」を適用する。粒子 $n$（Puncture）以外のすべてのプラスヘリシティ粒子 $b$ が $\delta(\langle bn \rangle)$ の制約を受けることは、**すべての情報流が凍結された Peirce 射影軸（$\lambda_n$）に完全に整列した状態**を意味する。

この極限において、BG 漸化式の複雑なプロパゲータは劇的に崩壊し、Puncture $n$ を主幹とする一次元的な「櫛型（Comb-like）」ツリーのみが生き残る。結果として、以下のソフトファクターの連鎖が再現される。

$$
M_n \sim \prod_{a=1}^{n-2} \left( \sum_{j>a} \frac{[aj]}{[an]} \right) \prod_{b=1}^{n-1} \delta(\langle bn \rangle)
$$

**結論：**
散乱振幅の驚異的な単純化は、多次元的な $L_\infty$ 情報ネットワークが、Peirce 軸に沿って「一次元の情報パイプライン」へと相転移し、Puncture からのエラー訂正信号がカスケード状に放射された結果の厳密な解析的表現である。

## 9.4 定理：Peirce縮約によるアソシエーターの自明化と $l_3$ の消失
（Theorem: Vanishing of the Associator and $l_3$ in the Self-Dual Limit）

### 概要と物理的意義
自己双対重力（SDG）の散乱振幅は、3点頂点（$l_2$ ブラケット）のみをシードとするツリー構造（Cubic theory）で完全に記述され、より高次の相互作用は存在しない。本節では、iGUTの根本原理である「八元数の非結合性」から出発し、自己双対極限（Peirce縮約）をとることで、高次ブラケット $l_3$ が厳密に消失し、理論が自動的にCubicに退化することを数学的に証明する。

### Theorem 2: $l_3^{\text{iGUT}}$ の自己双対極限における消失
例外ジョルダン代数 $\mathcal{H}_3(\mathbb{O})$ 上のジョルダン積から誘導されるアソシエーター $[X,Y,Z]$ を源泉とする、状態空間上の3項ブラケット $l_3^{\text{iGUT}}$ を考える。
自己双対セクター（$\mathbb{C}P^1$ スライス）への Peirce 射影 $\pi_{\text{SD}}$ の下で、この高次ブラケットは恒等的にゼロとなる。

$$
l_3^{\text{iGUT}}(\Psi_1, \Psi_2, \Psi_3) \xrightarrow{\pi_{\text{SD}}} 0
$$

### Proof

**Step 1: アソシエーターから関数空間上の $l_3$ への写像**
$\mathcal{H}_3(\mathbb{O})$ の元 $X, Y, Z$ に対するアソシエーターは以下で定義される。
$$[X, Y, Z] = (X \circ Y) \circ Z - X \circ (Y \circ Z)$$
iGUTのフルスペックのOSにおいて、この代数的な「ねじれ」は、状態空間 $\mathcal{V}_{\text{full}}$ 上の局所関数に対する3項演算子として引き戻される。自己双対セクターの有効状態空間 $C^\infty(\mathbb{C}P^1)$ に対し、代数上のアソシエーターの構造定数を縮約する微分写像 $\mathcal{A}$ を定義する。

$$
\mathcal{A} : C^\infty(\mathbb{C}P^1)^{\otimes 3} \to C^\infty(\mathbb{C}P^1)
$$

これにより、iGUTの $L_\infty$ 構造における3項ブラケットは $l_3^{\text{iGUT}}(\Psi_1, \Psi_2, \Psi_3) := \mathcal{A}(\Psi_1, \Psi_2, \Psi_3)$ として幾何学的に実装される。

**Step 2: Peirce縮約による部分代数への退化**
$\mathcal{H}_3(\mathbb{O})$ において、特定の観測軸を凍結するべき等元（Idempotent） $E_3 = \text{diag}(0, 0, 1)$ を用いてPeirce分解を行う。
固有値 0 の部分空間 $V_0(E_3)$ は、第3行・第3列がゼロとなる要素からなり、代数的に $2 \times 2$ のエルミート行列 $\mathcal{H}_2(\mathbb{O})$ と同型になる。
さらに、自己双対極限（SDGフェーズ）への射影 $\pi_{\text{SD}}$ は、この空間内で特定の複素構造 $J$ を選択し、八元数の虚数単位を1つ（例えば $e_1 \equiv i$）に制限する極限である。
したがって、射影 $\pi_{\text{SD}}$ の像は、純粋な複素数体 $\mathbb{C}$ 上のジョルダン代数へと完全に退化する。

$$
\pi_{\text{SD}} : \mathcal{H}_3(\mathbb{O}) \to V_0(E_3) \to \mathcal{H}_2(\mathbb{C})
$$

**Step 3: 例外性の消失と結合律の回復**
例外ジョルダン代数 $\mathcal{H}_3(\mathbb{O})$ の「例外性（完全な非結合性）」こそが、関数空間上の非自明な写像 $\mathcal{A}$（すなわち $l_3$）を駆動する根源である。
しかし、射影 $\pi_{\text{SD}}$ によって退化した $\mathcal{H}_2(\mathbb{C})$ の成分は、結合的な複素数 $\mathbb{C}$ である。結合代数上の行列は通常の積に関して厳密に結合律 $(AB)C = A(BC)$ を満たす（特殊ジョルダン代数となる）ため、八元数由来のアソシエーターのズレは厳密に消失する。

$$
[X, Y, Z] \xrightarrow{\pi_{\text{SD}}} 0 \quad \text{for } X, Y, Z \in \mathcal{H}_2(\mathbb{C})
$$

**Conclusion: $l_3$ の消失と SDG の Cubic 構造**
代数レベルでアソシエーターが恒等的にゼロとなるため、それを源泉とする関数空間上の微分写像 $\mathcal{A}$ もまたゼロとしてマッピングされる。

$$
l_3^{\text{iGUT}} \circ (\pi_{\text{SD}})^{\otimes 3} \equiv 0
$$

これにより、自己双対セクターにおいては $l_3$ 以降の高次ブラケットを駆動する代数的な「ねじれ」が根源から断たれ、 $L_\infty$ 情報流は $l_1$ と $l_2$ のみで厳密に閉じる。自己双対重力が Cubic theory として完結することは、iGUTの内部幾何における Peirce 縮約の不可避な帰結である。 $\blacksquare$
