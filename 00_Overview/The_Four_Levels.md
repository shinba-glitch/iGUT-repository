
# The Four Levels of iGUT: 創発の4階層

**informational Geometric Unified Theory の階層構造**

## はじめに：宇宙は「情報のOS」である

iGUT（informational Geometric Unified Theory）は、宇宙をあらかじめ用意された幾何学的舞台ではなく、**「情報を保存しようとする論理的アーキテクチャ」**として捉える。

私たちが観測している以下の要素は、宇宙の根源的レベルには存在しない。

* 時空
* 量子力学
* 素粒子
* 3世代構造
* 物理定数

これらはすべて、宇宙が極限のカオスから論理的整合性を取り戻すために行った冷却プロセス（エラー訂正）の果てに現れた**「創発現象」**である。iGUT はこの創発過程を 4つの階層（Level 1 → Level 4） として整理する。

---

## Level 1 — 創発する時空と量子力学

**(Emergent Spacetime & Quantum)**

我々が観測する現実の物理世界。Level 1 は、行列真空（Level 2）と残留ノイズ（Level 3）が組み合わさることで現れる。

* **時空の創発：$\mathbb{C}P^2$ 情報幾何**
安定した行列の真空（$\mathcal{H}_3(\mathbb{C})$）の rank-1 射影子空間は必然的に複素射影平面 $\mathbb{C}P^2$ となる。$\mathbb{C}P^2$ は 4次元の情報幾何であり、そのトポロジーが物理定数を決める。
* **量子力学の起源：残留ノイズ**
宇宙は完全には冷え切らず、Level 3 の非結合カオスの揺らぎが残る。この残留ノイズが非可換性を生む。
$$[x,p] = i\hbar$$


プランク定数 $\hbar$ とは、Level 3 の非結合カオスが残した化石である。
* **物理定数の決定**
$\mathbb{C}P^2$ 上の情報熱力学（Heat Kernel）とトポロジーから、以下の定数がパラメータなしで導出される。
* 微細構造定数：
$$\alpha^{-1} \approx 137.0363$$


* カビボ角：
$$\sin\theta_C \approx 0.2236$$





---

## Level 2 — 行列の谷底と代数的真空

**(The Algebraic Vacuum)**

Matrix Inflation（Level 3 の冷却）により、宇宙はアソシエーターがゼロになる絶対安定の谷底に落ちる。その谷底の数学的構造は 3×3 複素エルミート行列である。

$$\mathcal{H}_3(\mathbb{C})$$

* **3世代の起源：Peirce 分解**
$\mathcal{H}_3(\mathbb{C})$ の rank-3 構造により、互いに直交する原始冪等元は 3つだけ存在する。
$$P_i \circ P_j = \delta_{ij} P_i, \quad \sum_{i=1}^3 P_i = \mathbb{I}$$


素粒子が3世代なのは、宇宙が落ち着いた代数構造のランクが3だからである。
* **観測量の誕生**
Jordan 代数としての $\mathcal{H}_3(\mathbb{C})$ は、量子観測量（Hermitian operator）の一般化となる。

---

## Level 3 — 非結合カオスと力学の誕生

**(Non-Associative Chaos)**

Level 3 は、宇宙が初めて「合成（Composition）」を獲得した段階。しかし、この合成はまだ未熟で、結合法則すら成り立たない。

$$(x \circ y) \circ z \neq x \circ (y \circ z)$$

* **アソシエーター：原初のノイズ**
これは「情報の破壊量」を測る。
$$[x,y,z]_\circ = (x \circ y) \circ z - x \circ (y \circ z)$$


* **宇宙最初の作用：アソシエーターの抑制**
宇宙は情報を保存するために、非結合性（ノイズ）を最小化する方向へ進化する。
$$S_{\mathrm{assoc}} \sim \int \|[\Phi, \Phi, \Phi]_\circ\|^2$$


* **Matrix Inflation：宇宙の冷却**
Langevin 方程式に従い、宇宙は急速に冷却される。この冷却相転移こそが、iGUT におけるインフレーションである。
$$\mathcal{H}_3(\mathbb{O}) \longrightarrow \mathcal{H}_3(\mathbb{C})$$



---

## Level 4 — 原初の区別

**(Primordial Distinction)**

物理学の絶対的なゼロ地点。ここには以下のものは存在しない。

* 空間なし
* 時間なし
* 代数なし
* 幾何学なし

存在するのは、状態の集合 $\mathcal{S}$ と「同じか違うか」だけを判定するブール演算子のみである。

$$D(x,y) \in \{0,1\}$$

* **情報の公理（Axiom of Information）**
もし $D(x,z)=1$ なら、どんな $y$ を挟んでも以下の関係が成り立つ。
$$D(x,y)=1 \lor D(y,z)=1$$


これは「区別の保存則」であり、後の三角不等式や Fisher 情報計量の種となる。
* **Level 4 → Level 3：時間の誕生**
静的な区別ネットワークに、合成則 $\circ$ が導入されることでアルゴリズム的な時間が生まれる。

---

## まとめ：トップダウンでもボトムアップでもない。“根源からの創発”である。

従来の物理学は Level 1（幾何学・量子）を出発点にして、さらにミクロな世界を推測しようとしてきた。しかし iGUT は逆である。

* Level 4 の純粋な情報論理から出発し
* Level 3 の非結合カオスを経て
* Level 2 の行列真空に落ち着き
* Level 1 の物理世界が創発する

という**演繹的な創発プロセス**で宇宙を記述する。

👉 次は `01_Level_4_Information/Axioms_of_Distinction.md` に進み、宇宙の最初の構造である「区別の公理」を詳しく見ていこう。
