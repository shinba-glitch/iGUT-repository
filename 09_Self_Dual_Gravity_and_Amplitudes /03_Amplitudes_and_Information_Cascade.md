# 03. 散乱振幅と L_infinity 情報カスケード

## 1. 結合定数 $\kappa$ の固定とシードの一致
前稿の $L_\infty$-morphism により、iGUT のブラケットは SDG の運動学的なねじれ $[ij]$ を正確に生成する。
一般相対論（およびSDG）における 3点 MHVバー振幅との一致を要求することで、純粋な数学的定数であった $\kappa$ は物理的な重力結合定数として一意に固定される。
$$l_2(\Psi_i, \Psi_j) = \kappa [ij] \quad \implies \quad \kappa \equiv \sqrt{32\pi G}$$
これが、より高次の散乱振幅を再帰的に生成するツリーの完全なシード（種）となる。

## 2. 単一マイナス振幅と $\mathbb{C}P^1$ 上の Puncture
SDG において、オール・プラス振幅（純粋な自己双対セクター）はゼロとなるが、単一マイナス（single-minus）振幅は非ゼロの値を持つ。
iGUT において、これは次のように幾何学的に解釈される。
- **All-plus:** $\mathbb{C}P^1$ スライスが完全に滑らかで欠陥がない状態。位相的に自明であり振幅はゼロ。
- **Single-minus:** $\mathbb{C}P^1$ 上に 1 つのトポロジカル欠陥（Puncture）が存在する状態。この欠陥が $\mathfrak{sdiff}(S^2)$ に非自明なモノドロミーを生み、$w_{1+\infty}$ Ward 恒等式を駆動するソースとなる。

## 3. BG 漸化式から Decay Region 公式（ソフト積）への還元
iGUT のマスター方程式から導かれる Berends-Giele (BG) 漸化式に、Strominger らの論文における「Decay Region（半コリニア極限）」を適用する。

**【Peirce 軸への完全整列】**
粒子 $n$（Puncture）以外のすべてのプラスヘリシティ粒子 $b$ が、運動学的に $\delta(\langle bn \rangle)$ の制約を受ける。これは iGUT において、**すべての情報流が凍結された Peirce 射影軸（$\lambda_n$）に完全に整列した状態**を意味する。

**【櫛型ツリーへの崩壊と情報カスケード】**
この $\langle ab \rangle \to 0$ の極限において、BG 漸化式の複雑なプロパゲータ（ツリー和）は劇的に崩壊し、Puncture $n$ を主幹とする一次元的な「櫛型（Comb-like）」ツリーのみが生き残る。
各分岐ノードにおいて、頂点の $[aj]$ とプロパゲータの $1/[an]$ が結合し、以下のソフトファクターの連鎖（Strominger et al. の式(1)）が再現される。
$$M_n \sim \prod_{a=1}^{n-2} \left( \sum_{j>a} \frac{[aj]}{[an]} \right) \prod_{b=1}^{n-1} \delta(\langle bn \rangle)$$

**結論：**
散乱振幅の驚異的な単純化（Decay Region 公式）は、多次元的な $L_\infty$ 情報ネットワークが、Peirce 軸に沿って「一次元の情報パイプライン」へと相転移し、Puncture からのエラー訂正信号がカスケード状に放射された結果の厳密な解析的表現である。
