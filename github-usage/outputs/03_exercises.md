# GitHubの使い方 演習

## 1. 易しい演習

### 演習1
次の言葉を、自分の言葉で1文ずつ説明してください。

- Git
- GitHub
- リポジトリ

ヒント:
「何をするものか」に注目して書きます。

### 演習2
次のコマンドや作業を、自然な順番に並べてください。

- `git push origin main`
- ファイルを編集する
- `git clone https://github.com/example/study-notes.git`
- `git commit -m "READMEを更新"`

### 演習3
次のコードが何をしているか、各行を短く説明してください。

```bash
git add README.md
git commit -m "READMEを更新"
```

条件:
- 1行につき1文
- 「記録」という言葉を1回使う

## 2. 標準演習

### 演習4
次の場面を読んで答えてください。

場面:
あなたは自分のPCで `README.md` を1行修正して保存しました。しかし、GitHubの画面を見ると内容はまだ変わっていません。

質問:
なぜ変わっていないと考えられますか。`commit` と `push` の両方に触れて、2文以内で説明してください。

### 演習5
次の3行がそれぞれ何のためにあるか、初心者向けに説明してください。

```bash
git status
git add README.md
git commit -m "READMEを更新"
```

条件:
- 各行の役割を書く
- 3文以内にまとめる

### 演習6
Pull Request が役立つ理由を、次の場面に合わせて説明してください。

場面:
チームで使う手順書の内容を変更したいが、他の人に確認してから反映したい。

条件:
- 2文以内
- 「提案」または「確認」という言葉を使う

## 3. 応用演習

### 演習7
次の最小フローを読んで、1行ずつ役割を書いてください。

```bash
git clone https://github.com/example/study-notes.git
cd study-notes
git add README.md
git commit -m "READMEを更新"
git push origin main
```

条件:
- 5行すべてに説明を書く
- ローカル作業とGitHubとのやり取りの違いに触れる

### 演習8
次の誤解を正す短い説明文を書いてください。

誤解:
「`commit` したから、もうチーム全員に見えているはずだ」

条件:
- 3文以内
- `push` と GitHub に触れる

### 演習9
初めてGitHubを使う友人に向けて、「最初に覚えるべき3つのこと」を箇条書きでまとめてください。

条件:
- 用語の区別を1つ含める
- コード例に触れるなら短く書く
