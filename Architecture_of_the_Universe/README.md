# iGUT (Internal Geometric Unified Theory)
**The 3-Tier Categorical Architecture of the Universe (HW / OS / APP)**

## 📌 1. What is iGUT?（iGUTとは何か？）

iGUT は、物理学の現象を直接計算するための既存の理論ではなく、宇宙がどのような情報処理と論理で成り立っているかを示す**純粋数学的・概念的な「宇宙のフレームワーク」**である。

本プロジェクトは、宇宙を巨大な情報処理システムと見なし、その構造をソフトウェア・エンジニアリングにおける **「3層アーキテクチャ（ハードウェア・OS・アプリケーション）」** として完全に定式化する。

---

## 🏛 2. The 3-Tier Architecture（完全なる3層構造）

iGUT は以下の3つの独立したレイヤーによって構築される。

### ⚙️ Layer 1: HW (Mathematical Hardware) - 数学的ハードウェア層
OSを動作させるための「シリコン（実行環境・命令セット）」。物理的な基盤ではなく、純粋数学の公理系と基礎理論を提供する最下層のランタイム。
* **`hw-logic/`**: 直観主義論理、古典論理、部分対象分類子 $\Omega$。OSの「真理値」を支える論理ゲート。
* **`hw-category-theory/`**: 圏、関手、自然変換、モナド。OSの「宇宙方程式」を走らせるための基盤言語。
* **`hw-homotopy/`**: ホモトピー、鎖複体、 $L_\infty$ 代数の基礎。エラー訂正を行うためのトポロジー的土台。
* **`hw-algebra/`**: 例外リー群、八元数、ジョルダン代数。物質の種を生成するための代数的基盤。

### 🧠 Layer 2: OS (Core Kernel) - 宇宙のOS層
HW層の数学的命令セットを呼び出し、宇宙の論理構造（時間・物質・相互作用・空間）を制御するカーネル。
* **`core-algebra/`**: べき等元の選択と対称性の降下（ $F_4 \to Spin(9)$ ）。
* **`core-homotopy/`**: 結合律の破れの検知と、高次ブラケットによる整合性調整（Consistency Regulator）。
* **`core-category/`**: 忘却関手と随伴による「情報熱力学」と時間の矢の生成。
* **`core-topos/`**: 観測者の定義（幾何学的射）と、不確定性の起源。

### 🚀 Layer 3: APP (Physics Applications) - 物理アプリケーション層
OS層から提供されるメタ構造を読み込み、現実の物理学者が観測可能な「数値」や「現象」として出力する実験モジュール。
* **`app-kinematics/`**: OSの代数構造と物理的な運動量スピノルの翻訳辞書。
* **`app-amplitudes/`**: BG漸化式を用いた散乱振幅の計算と $l_3$ アノマリー（接触項）の抽出。
* **`app-scale-explorer/`**: 随伴のテンションから質量比やプランクスケールを第一原理で探索する数値実験モジュール。

---

## 🌌 3. The Unified Equation of Reality（宇宙のOS方程式）

OS層の中心で実行されるメインルーチンは、時間・物質・相互作用・空間を統合する以下の「圏論的宇宙方程式」として圧縮される。

$$
\text{Reality} = \underbrace{F \dashv U}_{\text{Flow and Generation}} + \underbrace{\ker(U)}_{\text{Matter}} + \underbrace{\eta}_{\text{Interaction}} + \underbrace{\mathrm{Rel}(\mathrm{im}(U), \ker(U))}_{\text{Space}}
$$

* **時間（ $\mathrm{im}(U)$ ）：** 忘却関手による情報の不可逆な押し流し。
* **物質（ $\ker(U)$ ）：** 忘却の過程で残った局所的な情報の固着。
* **相互作用（ $\eta$ ）：** 時間と物質の間の矛盾を縫い合わせる自然変換（ $L_\infty$ 補正）。
* **空間（ $\mathrm{Rel}$ ）：** 像と核の間に張られる関係性のネットワーク。

---

## 📂 4. Repository Structure（ディレクトリ構成）

```text
iGUT/
├── hw-logic/                ← 数学的ハードウェア（論理）
├── hw-category-theory/      ← 数学的ハードウェア（圏論）
├── hw-homotopy/             ← 数学的ハードウェア（ホモトピー）
├── hw-algebra/              ← 数学的ハードウェア（代数）
│
├── core-algebra/            ← OS層（対称性の降下）
├── core-homotopy/           ← OS層（整合性調整）
├── core-category/           ← OS層（情報熱力学と時間の矢）
├── core-topos/              ← OS層（観測者と内部論理）
│
├── app-kinematics/          ← APP層（キネマティクス辞書）
├── app-amplitudes/          ← APP層（振幅・接触項計算）
├── app-scale-explorer/      ← APP層（質量スケール探索）
│
└── OSAPPInterface.md        ← OSとAPPを繋ぐAPIドキュメント
