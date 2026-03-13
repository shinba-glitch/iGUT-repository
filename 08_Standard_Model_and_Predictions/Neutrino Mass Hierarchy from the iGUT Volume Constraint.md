# Neutrino Mass Hierarchy from the iGUT Volume Constraint
（iGUT の体積条件から導かれるニュートリノ質量階層）

本稿の目的は、前章で導かれた iGUT のニュートリノ質量スケール予言

$$ 
m_1 m_2 m_3 \simeq c_\nu^3,\quad c_\nu \simeq \frac{v^2}{M_P} \sim 0.025\ \text{eV}
$$

と、ニュートリノ振動実験で測定されている質量差

$$
\Delta m^2_{21} \equiv m_2^2 - m_1^2 \approx 7.5 \times 10^{-5}\ \text{eV}^2
$$

$$
|\Delta m^2_{31}| \equiv |m_3^2 - m_1^2| \approx 2.4 \times 10^{-3}\ \text{eV}^2
$$

を組み合わせることで、**質量階層が Normal か Inverted かを iGUT の内部から決着させる**ことである。

---

## 1. 体積条件：iGUT が課す「三つの質量の体積」

前章の Freudenthal 行列式の極値条件から、ニュートリノの 3 つの固有値（逆質量）と混合モードの三重積が一致することを得た。

$$
\lambda_1 \lambda_2 \lambda_3 = y_{12} y_{23} y_{13}
$$

逆質量仮説 $\lambda_i = c_\nu / m_i$ と、PMNS の大混合 $\Rightarrow y_{12} y_{23} y_{13} \sim \mathcal{O}(1)$ を用いると、

$$
m_1 m_2 m_3 \sim c_\nu^3
$$

となる。数値的には

$$
c_\nu \sim 0.025\ \text{eV} \quad \Rightarrow \quad m_1 m_2 m_3 \sim (0.025)^3 \approx 1.6 \times 10^{-5}\ \text{eV}^3
$$

---

## 2. Normal Hierarchy の検証

Normal Hierarchy（NH）では

$$
m_1 < m_2 \ll m_3
$$

であり、質量は

$$
m_2 = \sqrt{m_1^2 + \Delta m^2_{21}},\quad
m_3 = \sqrt{m_1^2 + \Delta m^2_{31}}
$$

と書ける。これを体積条件

$$
m_1 m_2 m_3 \simeq 1.6 \times 10^{-5}\ \text{eV}^3
$$

に代入して、$m_1$ を走らせてみる。

### 粗いオーダー評価

まず $m_1$ が極端に小さい場合（ $m_1 \to 0$）を考えると、

$$
m_2 \approx \sqrt{\Delta m^2_{21}} \approx 8.7 \times 10^{-3}\ \text{eV}
$$

$$
m_3 \approx \sqrt{\Delta m^2_{31}} \approx 5.0 \times 10^{-2}\ \text{eV}
$$

となり、

$$
m_1 m_2 m_3 \approx m_1 \times 8.7 \times 10^{-3} \times 5.0 \times 10^{-2}
\approx m_1 \times 4.4 \times 10^{-4}
$$

これが $1.6 \times 10^{-5}$ に一致するには

$$
m_1 \sim \frac{1.6 \times 10^{-5}}{4.4 \times 10^{-4}} \sim 3.6 \times 10^{-2}\ \text{eV}
$$

程度が必要になる。

この時点で既に、
* $m_1 \sim 0.03\text{–}0.04$ eV
* $m_2 \sim \sqrt{(0.03)^2 + 7.5 \times 10^{-5}} \sim 0.032\text{–}0.04$ eV
* $m_3 \sim \sqrt{(0.03)^2 + 2.4 \times 10^{-3}} \sim 0.055\text{–}0.06$ eV

という「**ほぼ準縮退（quasi-degenerate）に近い Normal Hierarchy**」が自然に現れる。

このときの質量和は

$$
\Sigma m_i \sim 0.03 + 0.033 + 0.058 \sim 0.12\ \text{eV}
$$

であり、宇宙論の上限 $\Sigma m_i \lesssim 0.12$ eV とギリギリ整合する領域に収まる。

---

## 3. Inverted Hierarchy の検証

Inverted Hierarchy（IH）では

$$
m_3 \ll m_1 \lesssim m_2
$$

であり、

$$
m_1 = \sqrt{m_3^2 + |\Delta m^2_{31}|},\quad
m_2 = \sqrt{m_3^2 + |\Delta m^2_{31}| + \Delta m^2_{21}}
$$

と書ける。

### $m_3 \to 0$ 近傍での評価

$m_3$ が極端に小さい場合、

$$
m_1 \approx \sqrt{2.4 \times 10^{-3}} \approx 5.0 \times 10^{-2}\ \text{eV}
$$

$$
m_2 \approx \sqrt{2.4 \times 10^{-3} + 7.5 \times 10^{-5}} \approx 5.1 \times 10^{-2}\ \text{eV}
$$

となるので、

$$
m_1 m_2 m_3 \approx (5.0 \times 10^{-2})(5.1 \times 10^{-2}) m_3 \approx 2.6 \times 10^{-3} \, m_3
$$

これが $1.6 \times 10^{-5}$ に一致するには

$$
m_3 \sim \frac{1.6 \times 10^{-5}}{2.6 \times 10^{-3}} \sim 6 \times 10^{-3}\ \text{eV}
$$

このとき、
* $m_3 \sim 0.006$ eV
* $m_1 \sim \sqrt{(0.006)^2 + 2.4 \times 10^{-3}} \sim 0.050$ eV
* $m_2 \sim 0.051$ eV

となり、質量和は

$$
\Sigma m_i \sim 0.006 + 0.050 + 0.051 \sim 0.107\ \text{eV}
$$

で、こちらも宇宙論の上限とは整合している。

---

## 4. どちらも「数値的には」生き残る —— では何が決定打になるのか？

ここまでの計算からわかる重要な事実は：

> **体積条件 $m_1 m_2 m_3 \sim c_\nu^3$ と振動データだけでは、Normal / Inverted の両方が「数値的には」許容される。**

つまり、単に「積」と「差」だけを見ている限り、両者とも iGUT の体積条件を満たす解を持つ。

では、iGUT は階層構造について何も言えないのか？  
答えは **No** だと思う。

iGUT には、まだ使っていない「もう一つの強力な拘束」がある：

- **逆質量シーソーと PMNS の大混合のリンク**
- **Freudenthal 行列式の符号・安定性条件（極値が極小か極大か）**

### 4.1. 大混合と「どの質量が一番軽いか」

逆質量シーソー

$$
\lambda_j \lambda_k = \|y_{jk}\|^2,\quad \lambda_i \propto \frac{1}{m_i}
$$

は、「軽いほど OS 上でよく伝播し、よく混ざる」という物語だった。

- Normal の場合：最も軽いのは $m_1$。しかし PMNS の観測事実では、「第 1 世代（電子ニュートリノ）」は必ずしも最大混合の中心ではない。
- Inverted の場合：最も軽いのは $m_3$。$m_1, m_2$ はほぼ同じ重さで、$m_3$ だけが少し軽い。この構造は、「2 つの重い状態が強く混ざり、1 つの軽い状態が少し浮いた位置にいる」という PMNS の実験的パターン（$\theta_{12}, \theta_{23}$ は大きく、$\theta_{13}$ はやや小さい）と自然に噛み合う。

iGUT 的に言えば：

> **「一つだけ軽い状態があり、それが他の二つと非対称な混ざり方をする」という構造は、Inverted Hierarchy の方が自然に実現される。**

### 4.2. Freudenthal 行列式の安定性と符号

Freudenthal 行列式

$$
\det(X_\nu) = \lambda_1 \lambda_2 \lambda_3 - \sum_i \lambda_i \|y_{jk}\|^2 + 2 y_{12} y_{23} y_{13}
$$

に対して、極値条件を課したとき、

$$
\det(X_\nu) \approx -2 \lambda_1 \lambda_2 \lambda_3 + 2 y_{12} y_{23} y_{13}
$$

となり、安定な真空（極小）を選ぶには、**体積項と三重積項のバランスが「押し合い」になる必要がある**。

- Normal の場合：3 つの質量が比較的近く、$\lambda_i$ も同程度になりやすい。すると $\lambda_1 \lambda_2 \lambda_3$ が大きくなりすぎ、三重積とのバランスを取るには微妙な調整が必要になる。
- Inverted の場合： $m_3$ が軽く、 $\lambda_3$ が大きくなる一方で、 $m_1, m_2$ はほぼ同じ重さで $\lambda_1 \approx \lambda_2$。この「2 対 1」の構造は、三重積 $y_{12} y_{23} y_{13}$ の符号構造と自然に噛み合い、安定な極小を作りやすい。

この点はまだ完全な数値解析ではないが、**「一つだけ軽い状態＋二つの準縮退状態」という Inverted 的な構造の方が、Freudenthal 行列式の安定性と PMNS の大混合パターンの両方と整合的である**という強い示唆を与える。

---

## 5. 暫定的結論：iGUT は Inverted Hierarchy を「好む」

現時点で iGUT が与えるメッセージをまとめると：

1. **体積条件と振動データだけでは、Normal / Inverted の両方が数値的には許容される。**
2. しかし、
   - 逆質量シーソーと PMNS の大混合の構造、
   - Freudenthal 行列式の安定性（極小構造）、
   を合わせて考えると、
   > **「一つだけ軽い状態＋二つの準縮退状態」という Inverted Hierarchy 的な構造の方が、iGUT の OS と自然に整合する。**

> **暫定予言（iGUT）：**
> ニュートリノの絶対質量スケールは $m^{(\nu)}_{\text{abs}} \sim 0.025$ eV であり、その階層構造は「Inverted Hierarchy」に近い準縮退スペクトルである可能性が高い。

この予言は、今後の精密宇宙論（$\Sigma m_i$ の測定）と次世代のニュートリノ実験（階層構造の決定）によって、直接的に検証されることになる。

