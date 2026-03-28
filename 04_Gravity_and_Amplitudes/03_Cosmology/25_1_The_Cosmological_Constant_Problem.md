# 25.1 The Cosmological Constant Problem and Unimodular Gravity: Explicit Calculation
（宇宙項問題とユニモジュラー重力：具体的な計算プロセス）

iGUTにおける「Level 3（非結合アソシエータ）からLevel 0への冷却過程における体積モードの凍結」が、数学的にどのようにユニモジュラー重力（Unimodular Gravity）へと射影され、120桁もの宇宙項問題（ $\Lambda_{\text{bare}} \sim \Lambda_{\text{NCG}}^4$ ）を無害化するのか。

その具体的な計算プロセスを、変分原理と微分幾何学に基づきステップバイステップで導出します。

---

## 1. スペクトル作用と巨大な「裸の宇宙項」

非可換幾何学のスペクトル作用 $S_{\text{spec}}$ の熱核展開から得られる、外部時空における有効作用（重力＋物質）は以下の形をとります。

$$
S = \int d^4x \sqrt{-g} \left[ \frac{1}{16\pi G} (R - 2\Lambda_{\text{bare}}) + \mathcal{L}_{\text{matter}} \right]
$$

ここで、 $\Lambda_{\text{bare}}$ は $a_0$ 項に由来する巨大なUV真空エネルギー（ $\sim \Lambda_{\text{NCG}}^4$ ）です。
通常の一般相対性理論では、計量 $g_{\mu\nu}$ のすべての成分を独立に仮想変分（ $\delta g_{\mu\nu}$ ）させるため、アインシュタイン方程式に $\Lambda_{\text{bare}}$ がそのまま現れ、宇宙を粉々に吹き飛ばすほどの膨張（120桁の矛盾）を予測してしまいます。

## 2. 体積モードの凍結（ユニモジュラー拘束条件）

iGUTの「冷却過程（忘却関手）」により、時空の根源的な体積自由度が凍結されます。これは数学的に、計量の行列式 $\sqrt{-g}$ が固定された背景体積形式 $\omega(x)$ （通常は局所的に $\omega(x) = 1$ ）に等しいという **ユニモジュラー拘束条件** として記述されます。

$$
\sqrt{-g} = \omega(x) = \text{const.}
$$

この拘束条件があるため、計量の変分 $\delta g_{\mu\nu}$ はもはや完全に自由ではありません。行列式の変分の公式 $\delta \sqrt{-g} = -\frac{1}{2}\sqrt{-g} g_{\mu\nu} \delta g^{\mu\nu}$ に拘束条件 $\delta \sqrt{-g} = 0$ を適用すると、**計量の変分は必ずトレースレス（無軌跡）でなければならない** という条件が得られます。

$$
g^{\mu\nu} \delta g_{\mu\nu} = 0
$$

## 3. トレースレス変分による $\Lambda_{\text{bare}}$ の完全な消失

この拘束条件のもとで、作用 $S$ の変分 $\delta S = 0$ を計算します。

$$
\delta S = \int d^4x \sqrt{-g} \left[ -\frac{1}{16\pi G} \left( R^{\mu\nu} - \frac{1}{2}g^{\mu\nu}R + \Lambda_{\text{bare}} g^{\mu\nu} \right) + \frac{1}{2}T^{\mu\nu} \right] \delta g_{\mu\nu} = 0
$$

ここで重要なのは、任意の $\delta g_{\mu\nu}$ ではなく、 $g^{\mu\nu} \delta g_{\mu\nu} = 0$ を満たす変分に対してのみ積分がゼロになるという点です。これは、大括弧 $[ \dots ]$ の中のテンソルの **トレース成分（対角和）が力学に一切寄与せず、トレースレス成分だけが方程式として残る** ことを意味します。

あるテンソル $A_{\mu\nu}$ のトレースレス成分 $\hat{A}_{\mu\nu}$ は、 

$$
\hat{A}_{\mu\nu} = A_{\mu\nu} - \frac{1}{4}g_{\mu\nu}A
$$

で定義されます。
これを用いて、左辺の幾何学テンソル（アインシュタイン・テンソル＋宇宙項）のトレースレス成分を計算します。

* 元のテンソル: $E_{\mu\nu} = R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R + \Lambda_{\text{bare}} g_{\mu\nu}$
* そのトレース: $E = g^{\mu\nu}E_{\mu\nu} = R - 2R + 4\Lambda_{\text{bare}} = -R + 4\Lambda_{\text{bare}}$

これを引き算してトレースレス成分を求めます。

$$
\hat{E}_{\mu\nu} = \left( R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R + \Lambda_{\text{bare}} g_{\mu\nu} \right) - \frac{1}{4}g_{\mu\nu} (-R + 4\Lambda_{\text{bare}})
$$

$$
\hat{E}_{\mu\nu} = R_{\mu\nu} - \frac{1}{4}g_{\mu\nu}R
$$

ここが核心です。**巨大な真空エネルギー $\Lambda_{\text{bare}}$ に $\frac{1}{4}g_{\mu\nu} \times 4\Lambda_{\text{bare}}$ が相殺し、完全に数式から消滅しました。**
右辺のエネルギー・運動量テンソル $T_{\mu\nu}$ についても同様にトレースレス成分を取ることで、以下の「トレースレス・アインシュタイン方程式」が得られます。

$$
R_{\mu\nu} - \frac{1}{4}g_{\mu\nu}R = 8\pi G \left( T_{\mu\nu} - \frac{1}{4}g_{\mu\nu}T \right)
$$

## 4. 積分定数としての「観測される宇宙項（ $\Lambda_{\text{obs}}$ ）」の創発

$\Lambda_{\text{bare}}$ が消えた方程式から、私たちが現在観測している微小なダークエネルギー（ $\Lambda_{\text{obs}}$ ）がどのように現れるのかを示します。
得られたトレースレス方程式の両辺に、共変微分 $\nabla^\mu$ を作用させます。

$$
\nabla^\mu \left( R_{\mu\nu} - \frac{1}{4}g_{\mu\nu}R \right) = 8\pi G \nabla^\mu \left( T_{\mu\nu} - \frac{1}{4}g_{\mu\nu}T \right)
$$

ここで、幾何学的なビアンキ恒等式（ $\nabla^\mu R_{\mu\nu} = \frac{1}{2}\nabla_\nu R$ ）と、エネルギー・運動量保存則（ $\nabla^\mu T_{\mu\nu} = 0$ ）を代入します。

$$
\frac{1}{2}\nabla_\nu R - \frac{1}{4}\nabla_\nu R = -8\pi G \left( \frac{1}{4}\nabla_\nu T \right)
$$

整理すると、以下の極めてシンプルな微分方程式になります。

$$
\nabla_\nu \left( R + 8\pi G T \right) = 0
$$

微分の結果がゼロになるということは、カッコの中身が時空全体で一定（定数）であることを意味します。この「積分定数」を $4\Lambda_{\text{obs}}$ と定義します。

$$
R + 8\pi G T = 4\Lambda_{\text{obs}}
$$

この結果を元のトレースレス方程式に代入して整理し直すと、最終的な重力場の方程式が得られます。

$$
R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R + \Lambda_{\text{obs}} g_{\mu\nu} = 8\pi G T_{\mu\nu}
$$

---

### 結論：iGUTによる宇宙項問題の解決

以上の計算から、以下の事実が数学的に証明されました。

1. **UV真空エネルギーの隔離:** 熱核展開の $a_0$ 項から生じる $\Lambda_{\text{NCG}}^4$ の巨大な真空エネルギー（ $\Lambda_{\text{bare}}$ ）は、体積モードの凍結（トレースレス変分）により、重力方程式の力学に一切結合しません。
2. **宇宙項の正体:** 方程式に現れる $\Lambda_{\text{obs}}$ は真空のエネルギー密度ではなく、共変微分を積分した際に生じる単なる「境界条件（積分定数）」です。

このように、iGUT の「忘却関手による体積モードの凍結」という幾何学的な洞察は、ユニモジュラー重力の数学的構造を通じて、理論物理学最大の謎である120桁の宇宙項問題を自然かつ完全に無害化します。
