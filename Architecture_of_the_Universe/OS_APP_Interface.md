# OS-APP Interface Specification
（iGUT: OS層とAPP層の接続インターフェース定義）

本ドキュメントは、iGUT の純粋数学的な「OS層（Core Kernel）」が生成する抽象構造を、「APP層（Physics Applications）」が物理的な観測量として受け取るための変換ルール（API）を定義する。

---

## 🔗 Interface 1: Spinor Kinematics Translation
**【接続元】** `core-algebra/` (例外ジョルダン代数の Peirce 分解)
**【接続先】** `app-kinematics/` (物理的な運動量スピノル変数 $\lambda, \tilde{\lambda}$ )
**【変換ルール】** OSが出力する自己双対ブロック $\mathcal{H}_2(\mathbb{C})$ とオフ対角ブロック $V_{1/2}$ の直和を、APPが「入出力状態（ヘリシティ）」としてどう解釈するかを規定する（Version 0 辞書）。

## 🔗 Interface 2: $L_\infty$ to Scattering Amplitudes
**【接続元】** `core-homotopy/` (整合性調整のための高次ブラケット $l_n$ )
**【接続先】** `app-amplitudes/` (BG漸化式と散乱振幅)
**【変換ルール】**
OSが発行する論理的バグの補正項（ $l_3$ ）を、APPが物理的な「3点接触相互作用の頂点（Vertex）」として漸化式ツリーにどう組み込むかを規定する。

## 🔗 Interface 3: Division Algebras to Gauge Groups
**【接続元】** `core-category/` (構成代数の次元降下と忘却関手 $U$ )
**【接続先】** `app-kinematics/DivisionAlgebra_GaugeHierarchy.md` (ゲージ群の創発デモ)
**【変換ルール】**
OSが情報を忘却する過程で生じる代数的な「核（ $\ker(U)$ ）」を、APPが標準模型のゲージ群 $SU(3) \times SU(2) \times U(1)$ としてどうマッピングするかを規定する。


## 🔗 Interface 3: Division Algebras $\to$ Gauge Groups (Forgetful Cascade Demo)

本セクションは、HW層の「構成代数」とOS層の「忘却関手」を結合し、APP層において「ゲージ群」を出力するためのインターフェースを定義する。
※ **【重要】** これは現実の物理定数を導出する第一原理計算ではなく、OS構造が物理的対称性をどのように創発するかを示す「概念的デモ（Conceptual Demo）」である。

* **OS 側入力（Input from Core）：**
  * HW基盤：構成代数の階層（ $\mathbb{O}, \mathbb{H}, \mathbb{C}, \mathbb{R}$ ）
  * OS処理：情報の粗視化を行う忘却関手 $U$
* **APP 側出力（Output to Physics）：**
  * 出力変数：標準模型のゲージ群 $SU(3) \times SU(2) \times U(1)$
  * 物理的意味：忘却プロセスによって残された対称性の化石（ $\ker(U)$ ）
* **実装モジュールへのリンク：**
  * 詳細なカスケードのメカニズムについては、[`app-kinematics/DivisionAlgebra_GaugeHierarchy.md`](./app-kinematics/DivisionAlgebra_GaugeHierarchy.md) を参照のこと。
