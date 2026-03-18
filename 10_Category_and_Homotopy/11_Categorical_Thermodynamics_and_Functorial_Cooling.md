# 11. Categorical Thermodynamics and Functorial Cooling
（圏論的熱力学と関手の縮退冷却）

本章では、iGUT のメタ・アーキテクチャである「関手の縮退冷却（Functorial Cooling）」を、純粋に数学的な情報熱力学（Information Thermodynamics）として再定義する。
ここで扱うのは、物理学の実験的宇宙論ではなく、圏論・代数・情報理論が交差する抽象的なトイモデルである。

目的は次の3点に集約される：

1. 忘却関手（Forgetful Functor）＝粗視化（Coarse-graining）
2. 関手のファイバーの大きさ＝エントロピー（Categorical Entropy）
3. 忘却関手の不可逆性＝時間の矢（Arrow of Time）

これらを数学的に定式化することで、「時間とは何か」「エントロピーとは何か」を圏論の言葉で再構築する。

---

## 1. Coarse-graining as a Forgetful Functor
（粗視化＝忘却関手）

高次圏 $\mathcal{C}$ を「ミクロの世界」、低次圏 $\mathcal{D}$ を「マクロの世界」とみなす。
忘却関手

$$
U : \mathcal{C} \to \mathcal{D}
$$

は、 $\mathcal{C}$ に存在した射・対称性・構造を「潰して」 $\mathcal{D}$ に写す。
これは統計力学における粗視化

$$
\text{microstates} \to \text{macrostates}
$$

の純粋な圏論的翻訳である。

---

## 2. Categorical Entropy
（圏論的エントロピー）

マクロ状態 $Y \in \mathcal{D}$ に対して、その逆像（ファイバー）

$$
U^{-1}(Y) = \{ X \in \mathcal{C} \mid U(X) = Y \}
$$

が「そのマクロ状態を実現するミクロ状態の集合」に対応する。
このファイバーの“情報量”を測ることで、関手 $U$ のエントロピーを定義する：

$$
S_U(Y) = \log |U^{-1}(Y)|
$$

これは John Baez らが提案した圏論的情報量（Categorical Information）の自然な一般化である。

---

## 3. Application to iGUT
（iGUT への適用）

iGUT のメタ構造は

$$
F_4 \longrightarrow Spin(9) \longrightarrow \mathrm{SDG}
$$

という「対称性の降下（Symmetry Descent）」で表される。

* **$F_4$：** 対象が1つしかない極限的な高対称圏
  $\to$ エントロピーはゼロ（完全秩序）
* **$Spin(9)$：** $E_3$ の選択により対象が分岐
  $\to$ エントロピーが立ち上がる（情報の爆発）
* **$\mathrm{SDG}$：** 複素部分代数への射影
  $\to$ さらに粗視化され、対象が増え、エントロピーが増大

このプロセスは、「関手の縮退冷却」＝「情報的ビッグバン」という数学的同値性を示す。

---

## 4. Arrow of Time as Irreversibility of Forgetful Functors
（時間の矢＝忘却関手の不可逆性）

忘却関手 $U : \mathcal{C} \to \mathcal{D}$ は一般に可逆ではない。

* 失われた射は戻らない
* 潰された対称性は復元できない
* ファイバーの情報は一意に再構成できない

宇宙には「外部」が存在しないため、この不可逆性は絶対的である。したがって、

$$
\text{Irreversibility of } U \iff \text{Arrow of Time}
$$

時間の矢とは、圏論的には「忘却関手の不可逆性」そのものである。

## 5. Adjunction and Entropy Generation
（随伴とエントロピー生成の関係）

前節までにおいて、時間の矢（エントロピー増大）を「忘却関手 $U$ による粗視化の不可逆性」として定義した。本節では、この冷却プロセスが単なる「一方通行の死（熱的死）」ではなく、宇宙の OS が動的平衡（Dynamic Equilibrium）を保つための**「随伴（Adjunction）」**の枠組みに完全に組み込まれていることを示す。

### 5.1 忘却関手 $U$ と 自由関手 $F$ の随伴ペア
圏論において、忘却関手 $U: \mathcal{C} \to \mathcal{D}$（構造を潰す関手）は、多くの場合、その左随伴として自由関手 $F: \mathcal{D} \to \mathcal{C}$（構造を生成する関手）を持つ。

$$
F \dashv U
$$

この随伴関係は、マクロな状態空間 $\mathcal{D}$ とミクロな状態空間 $\mathcal{C}$ の間に、以下のような自然な同型（1対1対応）を要求する。

$$
\mathrm{Hom}_{\mathcal{C}}(F(Y), X) \cong \mathrm{Hom}_{\mathcal{D}}(Y, U(X))
$$

### 5.2 圏論的「揺動散逸定理（Fluctuation-Dissipation）」
情報熱力学の観点から、この随伴ペア $F \dashv U$ は、非平衡統計力学における「揺動散逸定理」の純粋な圏論的表現として解釈できる。

* **右随伴 $U$（忘却・散逸）：** ミクロな状態 $X$ の詳細な構造を潰し、マクロな観測量 $Y$ へと射影する。これはエントロピー $S$ を増大させ、システムを安定な低エネルギー状態へと冷却・散逸（Dissipation）させる力である。
* **左随伴 $F$（自由生成・揺動）：** マクロな状態 $Y$ から、可能な限りのミクロな経路や構造を強制的に生成（Free generation）する。これはシステムに情報を持ち込み、微視的な揺らぎ（Fluctuation）やカオス（非結合性のバグなど）を生み出す力である。

### 5.3 自由エネルギー最小化の圏論的同値性
熱力学において、システムは自由エネルギー $F_{\text{thermo}} = E - TS$ を最小化するように振る舞う。これは「エネルギー $E$ を最小化しようとする力」と「エントロピー $S$ を最大化しようとする力」の均衡点である。

iGUT の OS において、この熱力学的な均衡条件は、まさに随伴の自然同型 $\cong$ そのものである。
> 宇宙の OS は、左随伴 $F$ によって「区別（情報量・エントロピー）を最大化」しようとするテンションと、右随伴 $U$ によって「経路のコスト（作用・バグ）を最小化」しようとするテンションの間に、常に同型関係 $\mathrm{Hom} \cong \mathrm{Hom}$ を成立させ続ける。

この意味で、iGUT における「自己双対重力（SDG）フェーズの安定性」とは、単なる代数的な静止状態ではなく、**左随伴（ $l_3$ バグの生成）と右随伴（ $L_\infty$ によるホモトピー収縮）が極限のバランスで拮抗している「圏論的な熱平衡状態（Categorical Thermal Equilibrium）」**に他ならないのである。
