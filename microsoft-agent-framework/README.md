# Microsoft Agent Framework

このテーマでは、Microsoft Agent Framework を使って AI エージェントを作るときの基本を学びます。最初の 1 体のエージェント作成から始めて、Tools、会話の状態管理、Memory、Workflow までを段階的に追います。

## 対象者
- AI エージェント開発をこれから学びたい初学者
- Python または C# のサンプルを読みながら理解したい人

## 含まれる教材一覧
- `outputs/01_overview.md`: 全体像と学習マップ
- `outputs/02_lesson.md`: 本編レッスン
- `outputs/03_exercises.md`: 段階式の演習
- `outputs/04_quiz.md`: 理解確認クイズ
- `outputs/05_answers.md`: 演習とクイズの答え
- `source/notes.md`: 公式情報の参照メモ
- `source/azure_openai_chat_client_sample.py`: AzureOpenAIChatClient を使う complete sample

## 学習の進め方
1. まず overview を読んで、Agent Framework の位置づけをつかみます。
2. 次に lesson を読み、最初のエージェントから Workflow まで順番に学びます。
3. exercises で手を動かし、quiz で理解を確認します。
4. 迷ったら answers と `source/notes.md` を見て公式情報に戻ります。

## AzureOpenAIChatClient を試す前の設定例
API キー方式で試すときは、まず次の環境変数を設定します。

```powershell
$env:AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
$env:AZURE_OPENAI_API_KEY="your-api-key"
$env:AZURE_OPENAI_DEPLOYMENT="gpt-4o-mini"
```

そのあとで `source/azure_openai_chat_client_sample.py` を読むと、接続設定とコードの対応が追いやすくなります。
