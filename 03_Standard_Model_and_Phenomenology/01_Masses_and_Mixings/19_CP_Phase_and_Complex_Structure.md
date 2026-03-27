# 19. CP Phase from the Complex Structure of CP²
（ $\mathbb{C}P^2$ の複素構造とCP位相の導出）

**【位置づけ】**
本ドキュメントは、これまでに実数構造として導出された質量階層およびカビボ角の枠組みを拡張し、標準模型におけるCP対称性の破れ（複素位相 $\delta$ ）の起源を特定する。
内部空間 $\mathbb{C}P^2$ のケーラー多様体としての性質、および四元数 $\mathbb{H}$ からの射影における非可換成分（ $j, k$ ）の残存効果を定式化し、CKM行列の複素位相とヤルスコグ不変量 $J$ が純粋な幾何学・代数構造から一意に導かれるメカニズムを構築する。

---

## 19.1 The Pure Imaginary Generators $\lambda_5, \lambda_7$ and Complex Rotation（ $\lambda_5, \lambda_7$ の純虚数成分と内部フレームの複素回転）

第13章で定義した通り、 $\mathbb{C}P^2 \cong SU(3)/(SU(2) \times U(1))$ のカルタン分解において、接空間（内部フレーム） $\mathfrak{m}$ を張る生成元は $\lambda_4, \lambda_5, \lambda_6, \lambda_7$ の4つである。
これらのゲルマン行列の数学的性質を分類すると、以下のようになる。

* **実対称行列:** $\lambda_4, \lambda_6$ （純粋な回転・混合を生成）
* **純虚数反対称行列:** $\lambda_5, \lambda_7$ （複素位相のシフトを生成）

内部空間の測地線に沿ったアップ系列とダウン系列のフレームのズレは、指数写像 $U = \exp(i \sum \theta^a \lambda_a)$ によって記述される。
系が $\lambda_5, \lambda_7$ の方向へ非ゼロの成分（ $\theta^5, \theta^7 \neq 0$ ）を持つとき、エルミート共役を用いたフレーム間の変換 $V_{\text{CKM}} = U_u^\dagger U_d$ には、いかなる基底の再定義（位相吸収）を行っても消去できない「物理的な複素位相」が必然的に残留する。これが、幾何学的観点から見たCP破れの必要条件である。

## 19.2 Quaternionic Leakage and the Imaginary Directions（非可換幾何学における虚方向の漏れ出し）

なぜ測地線は $\lambda_5, \lambda_7$ という「虚数方向」へのズレを持つのか。その根本原因は、Level 2 の非可換幾何学（四元数 $\mathbb{H}$ ）から Level 1 （複素数 $\mathbb{C}$ ）への忘却関手にある。

四元数代数は $\{1, i, j, k\}$ を基底とする。これを $\mathbb{C}$ の部分代数に射影する際、$1$ と $i$ は可換な複素平面にそのままマッピングされるが、非可換な $j, k$ 成分は $\mathbb{C}P^2$ 上の「余剰なフラックス（漏れ出し）」として振る舞う。
第17章で定義した内部ディラック演算子 $D_u$ の非対角成分 $\epsilon_{ij}$ は、単なる実数ではなく、この $j, k$ 方向の成分を含む四元数的な重みを持つ。

$$
\epsilon_{ij} = \epsilon_{ij}^{(R)} + i \epsilon_{ij}^{(I)} + j \epsilon_{ij}^{(J)} + k \epsilon_{ij}^{(K)}
$$

射影後、この $j, k$ 方向の非可換テンションは $\mathbb{C}P^2$ のケーラー形式（複素構造 $J$ ）と結合し、有効ポテンシャルにおいて純虚数の交差項を生み出す。これが $\lambda_5, \lambda_7$ 方向への「力」として作用し、フレームを複素平面外へとねじ曲げるのである。

## 19.3 Complex Correction to the Geometric Overlap Integral $k$（幾何学的重なり積分 $k$ に対する複素補正）

第18章で導出した幾何学的結合定数 $k$ は、純粋な実数としての重なり積分であった。

$$
k_{\text{real}} = F_{\text{geom}}(d) \exp\left( -\frac{d^2}{2\sigma^2} \right)
$$

しかし、ケーラー多様体である $\mathbb{C}P^2$ 上を波動関数が伝播するとき、測地線に沿った平行移動は「ホロノミー（Holonomy）」と呼ばれる位相の回転を伴う。これはアハラノフ＝ボーム効果の幾何学版に相当する。
閉曲線（3つの固定点を結ぶ測地線三角形）に沿ったホロノミーは、その三角形が囲むケーラー形式 $\omega$ の面積積分に等しい。したがって、オフダイアゴナルな結合定数 $k$ は、複素位相 $\delta_{\text{geom}}$ を伴う複素パラメータへと自然に拡張される。

$$
k_{\text{complex}} = k_{\text{real}} e^{i \delta_{\text{geom}}}
$$

この位相 $\delta_{\text{geom}}$ は、 $\mathbb{C}P^2$ のトーリック三角形の「幾何学的面積」と、四元数フラックスの結合定数によって厳密に決定される。

## 19.4 Analytic Formula for the CKM Complex Phase $\delta$（CKM行列の複素位相 $\delta$ の解析式）

複素化された結合定数 $k_{\text{complex}}$ を用いて、第16章の有効2×2（および完全な3×3）質量行列を再構築する。
オフダイアゴナル成分 $\epsilon_{u,d}$ は複素数となり、質量行列 $M^2$ は実対称行列からエルミート行列へと格上げされる。

$$
M^2 \sim \begin{pmatrix} m_1^2 & |\epsilon| e^{i\phi} \\ |\epsilon| e^{-i\phi} & m_2^2 \end{pmatrix}
$$

これを対角化するユニタリ行列 $U_u, U_d$ は複素成分を含む。アップ系列とダウン系列で質量（自己エネルギー $\alpha, \beta, \gamma$ ）が異なるため、対角化の際に生じる複素位相の回転量は両者で完全に一致することはなく、キャンセルされずに残る。
結果として構成される CKM行列 $V_{\text{CKM}} = U_u^\dagger U_d$ の標準パラメータ表示（PDG表示）におけるCP位相 $\delta_{\text{CP}}$ は、幾何学的なホロノミー位相 $\delta_{\text{geom}}$ と、各世代の質量差によって以下のような解析的関係を持つ。

$$
\delta_{\text{CP}} \approx \mathcal{F}\left( \delta_{\text{geom}}, \frac{\Delta m_u^2}{\Delta m_d^2} \right)
$$

## 19.5 Theoretical Prediction of the Jarlskog Invariant $J$（ヤルスコグ不変量 $J$ の理論値の予測）

標準模型においてCP破れの大きさを基底非依存に測る唯一の物理量はヤルスコグ不変量 $J$ である。

$$
J = \mathrm{Im}(V_{us} V_{cb} V_{ub}^* V_{cs}^*)
$$

iGUTの幾何学において、ヤルスコグ不変量は極めて直感的な幾何学的意味を持つ。それは、ユニタリティ三角形の面積の2倍であり、すなわち **「内部空間 $\mathbb{C}P^2$ 上で3つの固定点（世代）が張る測地線三角形の面積の、低エネルギー有効理論への射影」** そのものである。
四元数フラックスの漏れ出しと $\mathbb{C}P^2$ の体積積分から、ヤルスコグ不変量は理論的に以下のように予測される。

$$
J_{\text{theory}} \propto (k_{\text{real}})^6 \sin(\delta_{\text{geom}}) \prod_{i<j} \frac{\Delta m_{u, ij}^2 \Delta m_{d, ij}^2}{(M_W^2)^6}
$$

この公式は、「3世代すべてが揃わなければ面積が存在せず（ $J=0$ ）、CPは破れない」という小林・益川理論の要請を、 $\mathbb{C}P^2$ のトポロジー（固定点が正確に3つであること）として完全に証明するものである。
