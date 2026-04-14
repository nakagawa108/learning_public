# Microsoft Agent Framework Workflows 概要

## この教材で学ぶこと
この教材では、Microsoft Agent Framework の `Workflow` を使って、複数ステップの処理をどう組み立てるかを学びます。

単発の Agent に 1 回質問するだけなら、Workflow は不要なこともあります。  
一方で、次のような処理では Workflow が役立ちます。

- 要約してからレビューする
- 条件によって処理先を変える
- 複数の処理を並列に走らせて最後にまとめる
- 途中で人の承認を待ってから再開する

## まず押さえたい用語
### Agent
Agent は、モデルやツールを使って 1 つの対話や判断を行う実行単位です。

### Workflow
Workflow は、複数の実行単位を順番や条件つきでつなぐ設計図です。

### Executor
Executor は、Workflow の中の 1 ステップを担当する処理です。

### Edge
Edge は、どの Executor からどの Executor に処理が流れるかを表す接続です。

### Human-in-the-loop
Human-in-the-loop は、途中で人の入力や承認を受け取る仕組みです。

## どんな順番で学ぶか
1. Workflow が必要になる場面を知る
2. `Executor` と `Edge` の役割を理解する
3. 直列の最小 Workflow を読む
4. 条件分岐と並列実行を理解する
5. 状態管理、checkpoint、resume を理解する
6. Human-in-the-loop と Agent 連携を学ぶ

## 公式情報の現在地
2026-04-14 時点で、Microsoft Learn の Agent Framework ドキュメントでは `Agents` と `Workflows` が主要カテゴリとして案内されています。  
また、GitHub の公式 README では Workflows の特徴として、graph-based orchestration、streaming、checkpointing、human-in-the-loop、time-travel が紹介されています。

この教材では、その中でも特に「使い始めるために重要な考え方」に絞って整理します。

## この教材を読み終えるとできること
- Workflow を使うべき場面を説明できる
- 基本的な Workflow の流れを読める
- 直列、分岐、並列、集約の違いを説明できる
- 人の確認が必要な処理を Workflow に入れるイメージを持てる
