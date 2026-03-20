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
