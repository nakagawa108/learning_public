# Microsoft Agent Framework Workflows 教材設定

## テーマ名
Microsoft Agent Framework Workflows

## 想定読者
- Microsoft Agent Framework を触り始めた初学者
- Agent は少し見たが、Workflow の設計方法がまだ曖昧な人
- Python の基本文法は読めるが、ワークフロー指向の実装は初めての人

## 学習ゴール
- Workflow が何を解決する仕組みかを説明できる
- `Executor`、`Edge`、`WorkflowBuilder` の役割を区別できる
- 直列、分岐、並列、集約の基本パターンを読める
- Human-in-the-loop、checkpoint、resume の考え方を理解できる
- Agent を Workflow に組み込む場面と、Workflow を Agent 的に扱う場面を整理できる

## 教材出力物
- `README.md`
- `outputs/01_overview.md`
- `outputs/02_lesson.md`
- `outputs/03_exercises.md`
- `outputs/04_quiz.md`
- `outputs/05_answers.md`
- `source/notes.md`

## 文体
- 初学者向け
- 先に短い例を見せ、そのあとで意味を整理する
- 専門用語は最初に一文で定義する
- 1 セクション 1 概念を守る
- 難しい概念は「いつ使うか」から説明する

## 参照優先順位
1. `themes/microsoft-agent-framework-workflows/SKILL.md`
2. Microsoft Learn の Agent Framework 公式ドキュメント
3. Microsoft 公式 GitHub リポジトリ `microsoft/agent-framework`
4. `themes/microsoft-agent-framework-workflows/source/notes.md`
5. `themes/microsoft-agent-framework/` の既存教材

## 禁止事項
- 公式確認できない API 名や挙動を断定しない
- AutoGen や Semantic Kernel との比較を主役にしない
- いきなり高度な分散実行の話へ飛ばない
- コードを長くしすぎて、概念理解を邪魔しない
- Workflow を単なる「複数関数の連結」とだけ説明しない
