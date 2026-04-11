# GitHubの使い方 解答

## 演習の解答例

### 演習1
- Git: ファイルの変更履歴を記録して管理する仕組み
- GitHub: Gitで管理した内容をオンラインで共有しやすくするサービス
- リポジトリ: ファイルと変更履歴をまとめて管理する場所

### 演習2
正しい順番:
`git clone https://github.com/example/study-notes.git` → ファイルを編集する → `git commit -m "READMEを更新"` → `git push origin main`

補足:
実際には `git add README.md` が間に入ることが多いですが、この演習では大きな流れを確認しています。

### 演習3
解答例:
- `git add README.md`: `README.md` の変更を記録対象として選んでいる
- `git commit -m "READMEを更新"`: 選んだ変更を「READMEを更新」という説明つきで記録している

### 演習4
解答例:
PCで保存しただけでは、まだローカルで変更しただけの状態です。`commit` で記録し、`push` でGitHubへ送らないと、GitHubの画面には反映されません。

### 演習5
解答例:
`git status` は今の変更状態を確認するためのコマンドです。`git add README.md` は `README.md` の変更を記録対象にする操作で、`git commit -m "READMEを更新"` はその変更を履歴として残す操作です。

### 演習6
解答例:
Pull Request を使うと、変更を本体へ入れる前に提案して確認してもらえます。チームで安全に更新したいときに役立ちます。

### 演習7
解答例:
- `git clone https://github.com/example/study-notes.git`: GitHub上のリポジトリをローカルへコピーする
- `cd study-notes`: 作業するフォルダへ移動する
- `git add README.md`: ローカルで直した `README.md` を記録対象にする
- `git commit -m "READMEを更新"`: そのローカル変更を履歴として残す
- `git push origin main`: ローカルの記録をGitHubへ送る

### 演習8
解答例:
`commit` はローカルで変更を記録しただけです。まだ GitHub には送られていないので、チーム全員には見えていないことがあります。`push` してはじめて GitHub 上で共有されます。

### 演習9
解答例:
- Gitは履歴を管理する仕組みで、GitHubはその履歴を共有しやすくするサービス
- 基本の流れは `clone` → 編集 → `commit` → `push`
- Pull Request は変更を取り込んでほしいと提案する場

## クイズの答え

### 問題1
A

### 問題2
B

### 問題3
B

### 問題4
B

### 問題5
A

### 問題6
B

### 問題7
B

## まとめ
- GitとGitHubの違いを区別できると、学習の土台が安定します
- `clone`、`add`、`commit`、`push` はそれぞれ役割が違います
- Pull Request は、変更を安全に共有して確認するための仕組みです
