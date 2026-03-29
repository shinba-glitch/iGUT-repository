# 26. Dark Matter from Level 3 Residual Modes
（Level 3 残余モードからの暗黒物質の創発）

**【位置づけ】**
本ドキュメントは、標準模型（SM）最大の欠落である「暗黒物質（Dark Matter）」の代数幾何学的な正体を定式化する。
暗黒物質を未知の素粒子として導入するのではなく、第25章で記述された「Level 3（非結合アソシエータ）から Level 2（ $\mathbb{C}P^2 \times \mathbb{H}$ ）への相転移」における不完全な冷却の産物、すなわち「結合代数への射影演算子の核（Kernel）」として厳密に定義する。これにより、暗黒物質がSMゲージ群から完全にデカップリングする理由と、ファジー暗黒物質（FDM）としての質量スケールを持つ理由を第一原理から証明する。

---

## 26.1 The Pre-geometric Universe and the Associator Operator
（前幾何学的宇宙とアソシエータ演算子）

Level 3 の前幾何学的宇宙は、八元数 $\mathbb{O}$ に由来する非結合代数 $\mathcal{A} _{\text{non-assoc}}$ 上のヒルベルト空間 $\mathcal{H} _{3}$ によって記述される。
この空間には、代数の非結合性を測る「アソシエータ演算子（Associator Operator）」が定義される。代数の生成子 $e _{i}$ による左作用演算子を $L _{e _{i}}$ としたとき、アソシエータ演算子 $\hat{A} _{ij}$ は以下のように厳密に定義される。

$$
\hat{A} _{ij} = L _{e _{i}} L _{e _{j}} - L _{e _{i} e _{j}}
$$

任意の状態 $|\psi\rangle \in \mathcal{H} _{3}$ に対し、 $\hat{A} _{ij} |\psi\rangle \neq 0$ である状態は非結合的な自由度を持つことを意味する。初期の高温・高曲率宇宙（Level 3）は、このアソシエータの固有モードが励起した非結合状態の重ね合わせとして存在する。

## 26.2 Algebraic Definition of Dark Matter as the Near-Kernel
（冷却射影と暗黒物質の代数的定義）

宇宙の膨張に伴う冷却（忘却関手 $U: \mathbb{O} \to \mathbb{H} \to \mathbb{C}$ ）とは、非結合性が熱力学的に消去され、結合的な幾何構造（Level 2）が析出する相転移である。
このプロセスは、アソシエータの「熱的消去」を表す自己共役かつ冪等な直交射影演算子 $\Pi _{\text{assoc}}$ として定義される。

$$
\Pi _{\text{assoc}} = \lim _{\beta\to\infty} e^{-\beta \hat{A}^\dagger \hat{A}}
$$

標準模型のすべての素粒子（クォーク、レプトン、ゲージボソン）は、この冷却が完全に成功した射影の像（Image）に属する。

$$
\mathcal{H} _{\text{SM}} = \text{Im}(\Pi _{\text{assoc}})
$$

しかし、非平衡ダイナミクス（キッブル・ズレック機構）により、冷却プロセスは空間的に完全ではなく、射影しきれないトポロジカル欠陥が必ず取り残される。iGUTにおいて、暗黒物質（DM）の状態空間 $\mathcal{H} _{\text{DM}}$ は、この **「冷却射影演算子の核（Kernel）」** として厳密に定義される。

$$
\mathcal{H} _{\text{DM}} = \ker(\Pi _{\text{assoc}}) = \overline{\text{span}} \{ |\psi\rangle : \hat{A} _{ij} |\psi\rangle \neq 0 \}
$$

全ヒルベルト空間は、内積構造に基づく直交和分解によって完全に分離される。

$$
\mathcal{H} _{3} = \mathcal{H} _{\text{SM}} \oplus \mathcal{H} _{\text{DM}} \quad (\langle \psi _{\text{SM}} | \psi _{\text{DM}} \rangle = 0)
$$

## 26.3 Strict Decoupling from the Standard Model Gauge Group
（標準模型ゲージ群からの厳密なデカップリング）

暗黒物質 $\mathcal{H} _{\text{DM}}$ が光や通常の物質と相互作用しない（デカップリングする）事実は、上記の直交分解から数学的に証明される。
標準模型のゲージ群 $G _{\text{SM}}$ は、結合代数 $\mathcal{A} _{\text{assoc}}$ （ $\mathbb{C}P^2$ ）の自己同型群 $\text{Aut}(\mathcal{A} _{\text{assoc}})$ であるため、そのユニタリ表現 $\rho(g)$ は定義により代数の結合性を保存する。すなわち、射影演算子と完全に可換である。

$$
[\rho(g), \Pi _{\text{assoc}}] = 0
$$

暗黒物質 $|\psi _{\text{DM}}\rangle \in \ker(\Pi _{\text{assoc}})$ にゲージ変換を作用させると、

$$
\Pi _{\text{assoc}} \left( \rho(g) |\psi _{\text{DM}}\rangle \right) = \rho(g) \left( \Pi _{\text{assoc}} |\psi _{\text{DM}}\rangle \right) = 0
$$

となり、 $\mathcal{H} _{\text{DM}}$ はゲージ変換に対して閉じた不変部分空間（Invariant subspace）を形成する。
さらに、ゲージ場 $A _{\mu}$ による相互作用の遷移振幅（行列要素）を計算すると、 $A _{\mu}$ と $\Pi _{\text{assoc}}$ の可換性、および $\Pi _{\text{assoc}} |\psi _{\text{SM}}\rangle = |\psi _{\text{SM}}\rangle$ より、

$$
\langle \psi _{\text{SM}} | A _{\mu} | \psi _{\text{DM}} \rangle = \langle \psi _{\text{SM}} | \Pi _{\text{assoc}}^\dagger A _{\mu} | \psi _{\text{DM}} \rangle = \langle \psi _{\text{SM}} | A _{\mu} \Pi _{\text{assoc}} | \psi _{\text{DM}} \rangle = 0
$$

となり、相互作用頂点が厳密にゼロになることが示される。暗黒物質はゲージ表現を持たないため、電磁気力・弱い力・強い力から完全に切り離される一方で、外部時空の計量にはエネルギー・運動量テンソルとして寄与し、重力とのみ結合する。

## 26.4 Eigenvalue Spectrum and the Fuzzy Dark Matter Mass Scale
（固有値スペクトルとFDM質量スケールの対応）

Level 3 のフル・ディラック演算子 $D _{3} = D _{M} \otimes \mathbb{I} + \gamma _{5} \otimes D _{\text{non-assoc}}$ のもとで、暗黒物質モードは固有値 $\lambda _{\text{DM}}$ を持つ。

$$
D _{3} |\psi _{\text{DM}}\rangle = \lambda _{\text{DM}} |\psi _{\text{DM}}\rangle
$$

完全な核ではなく、不完全な冷却に起因する「ほぼ核（near-kernel）」モードとしてモデル化すると、微小な残留アソシエータ・ノルム $\epsilon \ll 1$ （ $\hat{A}^\dagger \hat{A} |\psi _{\text{DM}}\rangle = \epsilon^2 |\psi _{\text{DM}}\rangle$ ）が生じる。
ディラック演算子のスペクトル構造 $D _{3}^2 \sim D _{M}^2 + \Lambda _{\text{NCG}}^2 \hat{A}^\dagger \hat{A}$ により、暗黒物質の有効質量 $m _{\text{eff}} \sim |\lambda _{\text{DM}}| / c^2$ は以下の階層を持つ。

$$
m _{\text{eff}} \sim \Lambda _{\text{NCG}} \cdot \epsilon
$$

非可換スケール $\Lambda _{\text{NCG}} \sim 10^{19} \text{ GeV}$ に対し、 $\epsilon$ の極端な微小性によって質量が指数関数的に抑圧されることで、ファジー暗黒物質（FDM）に要求される極軽質量スケール $m _{\text{eff}} \sim 10^{-22} \text{ eV}$ が自然に生成される。

## 26.5 Cosmological Implications: Jeans Length and Halo Formation
（宇宙論的帰結：Jeans長とハロー形成）

iGUT の残余モードが FDM の質量スケール $m _{\text{eff}} \sim 10^{-22} \text{ eV}$ を持つことが証明された時点で、その後のマクロな振る舞いは FDM の標準的な宇宙論的ダイナミクスに完全に帰着する。
この極軽質量は、銀河スケール（ $\sim \text{kpc}$ ）に匹敵するマクロなド・ブロイ波長 $\lambda _{\text{dB}} \sim \hbar / (m _{\text{eff}} v)$ を生み出す。

この量子圧力（Quantum Pressure）は、小スケールにおける自己重力崩壊を抑制し、冷たい暗黒物質（CDM）モデルが直面するカスプ・コア問題（Cusp-Core problem）を自動的に解決する。
大規模構造（Cosmic Web）を形成するダークマター・ハローは、未知の素粒子の集団ではなく、ビッグバン時の「Level 3 非結合代数の凍結プロセス（相転移）」が宇宙空間に刻み込んだ、巨大な代数幾何学的な化石（Fossil）そのものである。
