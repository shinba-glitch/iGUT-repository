# 01. iGUTにおける自己双対重力（SDG）フェーズの定義

## 1. 概要
iGUT（Internal Geometric Unified Theory）において、現代の散乱振幅理論で議論される「自己双対重力（Self-Dual Gravity; SDG）」は、独立した理論ではなく、フルスペックの $L_\infty$ ネットワークが特定の極限において「凍結」された一種の低エネルギー・フェーズ（あるいは部分セクター）として定義される。
本稿では、iGUTの基礎代数からSDGの舞台となる「天球」と「キネマティック代数」がどのように創発するかを幾何学的に定式化する。

## 2. Peirce 縮約と天球 $\mathbb{C}P^1$ の必然性
iGUTの代数的真空は例外ジョルダン代数 $\mathcal{H}_3(\mathbb{O})$ であり、その内部幾何は $\mathbb{C}P^2$（あるいはその実多様体としての表現）に対応する。
SDGにおける「片ヘリシティのみが励起された状態」という物理的境界条件は、iGUTにおいては特定の Peirce 射影軸（例：$P_3$）の凍結として解釈される。
この Peirce 縮約により、有効な状態空間は以下のように崩壊する。
$$\mathcal{H}_3(\mathbb{O}) \xrightarrow{\text{Peirce Reduction}} \mathcal{H}_2(\mathbb{C}) \implies \mathbb{C}P^2 \to \mathbb{C}P^1$$

**【天球の内部幾何学的起源】**
この結果現れる $\mathbb{C}P^1 \cong S^2$ スライスこそが、Stromingerらをはじめとする Celestial Holography で「無限遠の境界」として扱われていた**「天球（Celestial Sphere）」の正体**である。天球は外部時空に設けたスクリーンではなく、微視的な情報幾何の有効位相面として必然的に現れる。

## 3. 非結合性からハミルトン流（$w_{1+\infty}$）への移行
$\mathcal{H}_3(\mathbb{O})$ の特徴である非結合性（アソシエーター）は、内部微分 $\mathfrak{f}_4$ を生成する。Peirce 縮約と複素構造の選択の下で、この代数的な歪みは $\mathbb{C}P^1$ スライス上への射影において、フビニ・スタディ計量 $\omega_{FS}$ に伴う面積保存微分同相群 $\mathfrak{sdiff}(S^2)$ を生成するハミルトンベクトル場として作用する。
これにより、有効な結合則（$l_2$ ブラケット）は $\mathbb{C}P^1$ 上のポアソン括弧 $\{\cdot, \cdot\}_{FS}$ へと退化し、これが自己双対重力における無限次元対称性 $w_{1+\infty}$ を駆動する源泉となる。
