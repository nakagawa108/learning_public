# Microsoft Agent Framework Workflows 解答

## 演習の解答例

### 演習 1
1. 単発でメール件名を 1 行提案する  
   Agent 単体向きです。1 回の応答で終わるためです。
2. 問い合わせを分類し、担当部署に振り分ける  
   Workflow 向きです。分類と分岐があるためです。
3. 原稿を 3 観点で並列レビューし、最後に総合コメントを作る  
   Workflow 向きです。Fan-out と Fan-in が合います。
4. 契約申請をチェックし、不足があれば人に確認してから再開する  
   Workflow 向きです。Human-in-the-loop と checkpoint/resume が必要です。

### 演習 2
解答例:
- `summarize_notes`
- `extract_actions`
- `draft_report`

理由:
- 要点整理
- 行動項目抽出
- 最終文面作成

の 3 つは役割が違うからです。

### 演習 3
解答例:
- 分類 Executor: `classify_ticket`
- 分岐先 Executor:
  - `handle_billing`
  - `handle_technical`
  - `handle_other`

説明:
- `classify_ticket` の結果を見て、条件つき Edge が各担当 Executor に流します。

### 演習 4
解答例:
- Fan-out する場所: 提案書を受け取った直後
- 並列 Executor:
  - `fact_check`
  - `style_check`
  - `risk_check`
- Fan-in する場所: 3 つのレビュー結果がそろったあと
- 最後の Executor: `final_review`

考え方:
- 各観点は独立しているので並列化しやすいです。
- 最後に 1 つへ集約して、人が読みやすい形へまとめます。

### 演習 5
解答例:
- 確認を入れる段階: 入力検証の直後
- 保存する状態:
  - `travel_date` があるか
  - `amount` があるか
  - 申請 ID

checkpoint が必要な理由:
- 人の返答を待つ間に Workflow を一時停止し、同じ処理を最初からやり直さずに続きから再開したいからです。

### 演習 6
解答例:
- `classify_request`
- `summarize_request`
- `check_approval_needed`
- `send_notification`

分けた理由:
- どこで失敗したか見やすくなる
- 分岐や途中停止を入れやすくなる

### 演習 7
解答例:

```python
# 概念がわかることを目的にした擬似コード
builder = WorkflowBuilder()

builder.add_executor("classify")
builder.add_executor("request_approval")
builder.add_executor("summarize")
builder.add_executor("finalize")

builder.add_conditional_edge("classify", "request_approval", when="urgent")
builder.add_conditional_edge("classify", "summarize", when="normal")
builder.add_edge("summarize", "finalize")
builder.add_edge("request_approval", "finalize")

# urgent の場合は承認前に checkpoint を作成
# 承認結果が届いたら resume して finalize へ進む
```

ポイント:
- `classify` が判断材料を作る
- Edge が進み先を決める
- 承認待ちの前後で checkpoint/resume を考える

## クイズの答え
1. 2  
Workflow は複数ステップの流れを制御する仕組みです。

2. 2  
Executor は 1 ステップの実行単位です。

3. 2  
Edge は処理の流れ先を表します。

4. 3  
分類、分岐、承認待ちは Workflow 向きの典型です。

5. 1  
複数観点の並列評価では Fan-out / Fan-in が役立ちます。

6. 1  
Checkpoint は途中状態の保存と再開のために使います。

7. 1  
不足情報の回収や承認依頼で Human-in-the-loop が活きます。

8. 2  
Workflow が流れを管理し、Agent はステップ内の判断担当になれます。

9. 2  
最初は最小構成で始める方が理解もしやすく失敗しにくいです。

10. 1  
途中の分類結果は後続判断に使う状態です。

## 仕上げの確認ポイント
- `Executor` と `Edge` を自分の言葉で説明できるか
- Workflow を使うべき場面を 2 つ以上挙げられるか
- Human-in-the-loop と checkpoint の関係を説明できるか
- Agent と Workflow の役割分担を説明できるか
