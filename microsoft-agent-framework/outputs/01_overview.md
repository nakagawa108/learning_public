# Microsoft Agent Framework 学習ガイド

## 1. Microsoft Agent Framework とは
Microsoft Agent Framework は、AI エージェントやマルチステップのワークフローを作るためのフレームワークです。

たとえば、
- 質問に答えるチャットエージェントを作る
- 必要に応じて関数や API を呼ぶ
- 会話の流れをまたいで文脈を覚える
- 複数の処理を順番につないで動かす

といったことを 1 つの考え方で扱いやすくします。

要点:
- AI エージェントを作るための土台
- 会話型の処理と、明示的な処理フローの両方を扱える

## 2. まず押さえる 2 つの柱
### Agent
Agent は、LLM を使って入力を解釈し、必要ならツールを使って応答する実行主体です。

例:
- ユーザーの質問に答える
- 天気取得ツールを呼ぶ
- 会話履歴を見ながら返答する

### Workflow
Workflow は、処理の順番や分岐をあらかじめ決めて組み立てる仕組みです。

例:
- 入力を受ける
- 要約する
- レビューする
- 結果だけ返す

要点:
- `Agent` は柔軟に考えて動く側
- `Workflow` は流れを明示的に組む側

## 3. どんな順番で学ぶか
この教材では次の順で学びます。

1. 最小のエージェントを作る
2. Tools を追加する
3. Session で会話の流れを保つ
4. Memory で継続的な文脈を扱う
5. Workflow で複数処理をつなぐ

この順番にすると、「1 回答えるだけのエージェント」から「流れを持つアプリ」へ自然に進めます。

要点:
- いきなり複雑な構成に行かず、1 つずつ機能を積み上げる

## 4. このテーマでのゴール
読み終えるころには、次のことができる状態を目指します。

- Agent Framework の全体像を言葉で説明できる
- Agent と Workflow の違いを説明できる
- 公式チュートリアルのどこを読めばよいか分かる
- 次に自分で試すべき最小サンプルを決められる

## 5. 2026-04-10 時点で知っておきたいこと
公式ドキュメントでは、Microsoft Agent Framework は 2026-02-20 更新の overview で public preview と案内されています。

つまり、
- 今まさに育っているフレームワークである
- ドキュメントや API が今後変わる可能性がある
- 学習時は公式 Learn と GitHub を確認する習慣が大切

要点:
- 教材だけで固定せず、公式情報とセットで学ぶ

## 6. AutoGen と Semantic Kernel との違い
Microsoft Learn の 2026-02-20 更新 overview では、Microsoft Agent Framework は AutoGen と Semantic Kernel の direct successor と説明されています。

ここで大事なのは、Agent Framework がまったく別系統の新製品というより、AutoGen と Semantic Kernel の流れを引き継いで統合した位置づけだという点です。

### AutoGen との違い
AutoGen は、複数エージェントのやり取りや、agent パターンを試しやすいことが強みでした。

Agent Framework はその流れを引き継ぎつつ、
- Agent の考え方を保つ
- Workflow で実行順序を明示できる
- state management を強める

という方向へ進んでいます。

ひとことで言うと、
- AutoGen: agent 同士の協調を試しやすい
- Agent Framework: それに加えて制御性と運用性を高めた形

### Semantic Kernel との違い
Semantic Kernel は、AI 機能をアプリへ組み込むための SDK として、
- plugin
- filter
- memory
- telemetry
- 型安全性

のような enterprise 向け要素が強みでした。

Agent Framework はその強みを受け継ぎつつ、
- Agent
- Workflow
- Session
- Context Provider
- telemetry や state management

を 1 つの学習文脈にまとめています。

ひとことで言うと、
- Semantic Kernel: AI 機能をアプリに組み込む基盤色が強い
- Agent Framework: Agent と Workflow を中心にした統合的な入口

要点:
- AutoGen の分かりやすい agent 抽象と、Semantic Kernel の enterprise 向け機能を合わせた理解が近い

## 7. 初学者はどう捉えるとよいか
これから新しく学ぶなら、まず Agent Framework を中心に置くのがおすすめです。

理由:
- 2026-02-20 の overview で direct successor と明示されている
- 2026-04-01 と 2026-04-02 に migration guide が公開されている
- Agent と Workflow を同じ文脈で学べる

AutoGen や Semantic Kernel を知っていると過去の資料は読みやすくなりますが、入口としては Agent Framework を主軸にしたほうが整理しやすいです。

要点:
- 新しく学ぶ主軸は Agent Framework
- AutoGen と Semantic Kernel は系譜として理解すると混乱しにくい

## まとめ
- Microsoft Agent Framework は、Agent と Workflow を中心に学ぶと理解しやすい
- 学習順は `最小エージェント -> Tools -> Session -> Memory -> Workflow`
- AutoGen と Semantic Kernel の流れを引き継ぐ direct successor として整理されている
- public preview なので、公式情報の確認が重要
