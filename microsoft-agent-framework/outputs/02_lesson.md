# Microsoft Agent Framework レッスン

## 1. 最初の用語整理
### Agent
Agent は、入力を受けて考え、必要ならツールを使いながら応答するプログラム部品です。

### Tool
Tool は、エージェントが外部の関数や API を使うための手段です。

### Session
Session は、会話の流れをまたいで文脈を保つ単位です。

### Memory
Memory は、履歴やユーザー情報のような継続データを扱う仕組みです。

### Workflow
Workflow は、複数の処理を順番や条件つきでつなぐ仕組みです。

要点:
- まず 5 つの語を区別すると読みやすくなる

## 2. 最小のエージェントを作る
いちばん小さい例は、「1 つの質問に答えるエージェント」です。

たとえば Python では、公式チュートリアルで `agent-framework --pre` を入れ、クライアントから `as_agent(...)` でエージェントを作り、`run(...)` で実行します。C# でも同様に、クライアントから `AsAIAgent(...)` でエージェントを作れます。

ここで大事なのは、細かい記法よりも次の流れです。

1. モデルを使うためのクライアントを用意する
2. エージェントに名前と instructions を与える
3. メッセージを渡して結果を受け取る

これは「ただの LLM 呼び出し」と似ていますが、あとから Tools や Session を足しやすい形になっているのが違いです。

### Python 例
```python
from agent_framework import AgentClient

# 1. モデル用クライアントを作る
client = AgentClient(model="gpt-4.1-mini")

# 2. エージェントを作る
agent = client.as_agent(
    name="study_helper",
    instructions="Python 学習の質問へ短く答えてください。"
)

# 3. 入力を渡して実行する
result = agent.run("Python のリストとは？")
print(result)
```

このコードで見てほしいのは、API の細部よりも「作る -> 指示する -> 実行する」の 3 段階です。

要点:
- 最初のゴールは、1 回の入力に返答できる状態を作ること

## 3. Tools を追加する
Tool は、エージェントの手足です。

例:
- 天気を返す関数
- 社内データを調べる関数
- Web 検索やファイル検索

公式の Step 2 では、関数をツールとして定義し、それをエージェントに渡す流れが紹介されています。

ここでの考え方はシンプルです。
- LLM は「考える」
- Tool は「外に取りに行く」

たとえば「東京の天気を教えて」と聞かれたとき、モデルが推測で答えるより、天気取得ツールを呼ぶほうが正確です。

### Python 例
```python
from agent_framework import AgentClient

def get_weather(city: str) -> str:
    return f"{city} is sunny"

client = AgentClient(model="gpt-4.1-mini")

agent = client.as_agent(
    name="weather_helper",
    instructions="天気の質問には、必要に応じて weather ツールを使ってください。",
    tools=[get_weather],
)

result = agent.run("東京の天気を教えて")
print(result)
```

この例では `get_weather` が Python の普通の関数です。Agent Framework では、その関数をエージェントのツールとして渡す形で考えると理解しやすいです。

要点:
- Tool は、モデルの推測ではなく外部の事実を扱うために使う

## 4. Session で会話をつなぐ
Session は、複数ターンの会話を 1 本の流れとして扱う仕組みです。

例:
1 回目: 「私の名前は Aiko です」
2 回目: 「私の名前を覚えていますか」

Session がなければ、2 回目だけ見たモデルは前の文脈を失いやすくなります。
公式の multi-turn チュートリアルでは、session を作って `run(...)` に渡し、会話履歴を保つ流れが示されています。

### Python 例
```python
from agent_framework import AgentClient, Session

client = AgentClient(model="gpt-4.1-mini")

agent = client.as_agent(
    name="memory_helper",
    instructions="会話の流れを見ながら答えてください。"
)

session = Session()

agent.run("私の名前は Aiko です", session=session)
result = agent.run("私の名前を覚えていますか", session=session)

print(result)
```

ポイントは、同じ `session` を 2 回とも渡していることです。ここが変わると、会話の流れも切れてしまいます。

要点:
- Session は「会話を続けるための入れ物」

## 5. Memory は Session より一歩進んだ仕組み
Memory は、会話履歴だけでなく、ユーザー情報や外部知識を文脈として注入する考え方です。

公式の Step 4 では、
- `InMemoryChatHistoryProvider` や `InMemoryHistoryProvider`
- custom history provider
- context provider

といった形で、履歴や追加情報を扱う方法が紹介されています。

たとえば、
- ユーザー名を覚える
- 好みを保持する
- 以前のやり取りを監査用に残す

といった用途です。

ここでの直感はこうです。
- Session: 会話の流れを保つ
- Memory: 会話に入れたい継続情報を管理する

### Python 例
```python
from agent_framework import AgentClient, Session

client = AgentClient(model="gpt-4.1-mini")

agent = client.as_agent(
    name="personal_helper",
    instructions="ユーザー情報を考慮しながら答えてください。"
)

session = Session()

# 学習用の簡易例:
# 実際には context provider や history provider で渡すことを考える
user_context = {
    "user_name": "Aiko",
    "favorite_language": "Python",
}

result = agent.run(
    "私におすすめの学習方法を教えて",
    session=session,
    context=user_context,
)

print(result)
```

この例の `user_context` は、「会話のその場だけ」ではなく「持ち越したい情報」を表すイメージです。実運用では公式ドキュメントの provider を使って整理していきます。

要点:
- Session と Memory は似て見えるが、役割は同じではない

## 6. Workflow で処理の順番を決める
Workflow は、処理の流れをグラフとして組み立てる仕組みです。

たとえば次のような流れを考えます。
1. 入力文を受け取る
2. 要約する
3. レビューする
4. 最終結果を返す

このように順番がはっきりしているなら、Agent 単体より Workflow のほうが向いています。

公式の Workflows 概要では、主な構成要素として次が紹介されています。
- Executors: 処理を担当する単位
- Edges: 単位どうしのつながり
- WorkflowBuilder: 全体の組み立て役

また、型安全、checkpointing、human-in-the-loop の考え方も重要です。

### Python 例
```python
# 学習用の疑似コード
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()

builder.add_executor("summarize")
builder.add_executor("review")
builder.add_edge("summarize", "review")

workflow = builder.build()
result = workflow.run("この文章を要約してレビューしてください")

print(result)
```

Workflow のコードは「何をどの順番で通すか」を読むためのものです。Agent 単体よりも、処理の道筋が見えやすいのが特徴です。

要点:
- 何をどの順番で動かすかを明示したいときは Workflow を使う

## 7. Agent と Workflow の使い分け
公式 overview でも、Agent と Workflow の使い分けが整理されています。

Agent が向く場面:
- 会話型である
- 多少の柔軟さが必要
- ツール利用をモデルに任せたい

Workflow が向く場面:
- 手順が決まっている
- 分岐や順序を制御したい
- 複数の処理や複数エージェントをつなぎたい

迷ったときは、次の問いが役立ちます。

「これは会話として考えさせたいのか、それとも手順として組みたいのか」

要点:
- 自律性を重視するなら Agent
- 制御性を重視するなら Workflow

## 8. 何から実際に試すとよいか
初学者には次の順番がおすすめです。

1. まず Step 1 の最小サンプルを動かす
2. Step 2 で天気ツールのような単純な関数を足す
3. Step 3 で session を使い、2 ターン会話を試す
4. Step 4 でユーザー情報を覚える context provider の例を読む
5. Step 5 で 2 ステップ workflow を組む

この順番なら、概念ごとに「何が増えたか」が見えやすくなります。

## 9. AzureOpenAIChatClient を使う場合
`AzureOpenAIChatClient` は、Azure OpenAI をバックエンドとして Agent Framework を使いたいときの Python クライアントです。

この形が向くのは、次のような場面です。
- すでに Azure OpenAI リソースとモデルデプロイを持っている
- Azure の認証基盤を使いたい
- OpenAI 互換 API ではなく、Azure 側の構成に合わせて学びたい

Microsoft Learn の Quick Start では Python 側の導入例として `AzureAIClient` も案内されていますが、GitHub 上の Python 例や API 名では `agent_framework.azure.AzureOpenAIChatClient` を使うパターンも確認できます。教材では「Azure OpenAI を直接使う学習用の形」としてこちらも押さえておくと理解しやすいです。

要点:
- Azure OpenAI を使う Python 学習では `AzureOpenAIChatClient` も重要な入口になる

## 10. AzureOpenAIChatClient の準備
まず必要なのは次の 3 つです。

1. Azure OpenAI リソース
2. デプロイ済みモデル名
3. 認証方法

認証は複数ありますが、この教材では従来の API キー方式で学びます。つまり、開発時は Azure OpenAI のキーを環境変数で持ち、コード側で `api_key` を渡す形です。

また、少なくとも次の値は整理しておくと分かりやすいです。
- Azure OpenAI の endpoint
- Azure OpenAI の api_key
- model deployment 名

たとえば環境変数で持つなら、次のように考えられます。

```python
import os

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
```

要点:
- `endpoint` `api_key` `deployment` を分けて意識する
- 教材ではまず API キー方式で学ぶ

## 11. AzureOpenAIChatClient で最小エージェントを作る
まずは Azure OpenAI に接続して、1 回だけ応答する最小例です。

### Python 例
```python
import os
from agent_framework.azure import AzureOpenAIChatClient

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

chat_client = AzureOpenAIChatClient(
    endpoint=endpoint,
    api_key=api_key,
    deployment_name=deployment,
)

agent = chat_client.create_agent(
    instructions="Python 学習の質問へ短く答えてください。"
)

result = agent.run("Python の辞書とは？")
print(result)
```

ここでの見方は、前半の一般例と同じです。

1. 今回は `AgentClient` ではなく `AzureOpenAIChatClient` を作る
2. そのクライアントから agent を作る
3. `run(...)` で実行する

違いは、モデル指定の前に Azure OpenAI の接続情報と API キー認証が入ることです。

要点:
- 一般形との違いは「Azure 接続情報」と「API キー」が増えること

## 12. AzureOpenAIChatClient で Tool を使う
`AzureOpenAIChatClient` を使っても、考え方は同じです。Agent にツールを渡せば、Azure OpenAI をバックエンドにしたエージェントが必要に応じてそれを使います。

### Python 例
```python
import os
from agent_framework.azure import AzureOpenAIChatClient

def get_weather(city: str) -> str:
    return f"{city} is sunny"

chat_client = AzureOpenAIChatClient(
    endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
)

agent = chat_client.create_agent(
    instructions="天気の質問では必要に応じて get_weather を使ってください。",
    tools=[get_weather],
)

result = agent.run("東京の天気を教えて")
print(result)
```

要点:
- クライアントが Azure 用になっても、Tool を足す考え方は変わらない

## 13. AzureOpenAIChatClient を使うときの見方
初学者が混乱しやすい点は、「何が Agent Framework 固有で、何が Azure 固有か」です。

次のように分けると整理しやすいです。

- Agent Framework 側の考え方
  - Agent
  - Tool
  - Session
  - Memory
  - Workflow

- Azure 側の考え方
  - endpoint
  - api_key
  - deployment

つまり、エージェント設計そのものは Agent Framework の学習で、接続先と認証情報が Azure の学習です。

要点:
- 設計の学習と、接続設定の学習を分けると理解しやすい

## 14. AutoGen と比べると何が違うか
AutoGen は、複数エージェントの会話や役割分担を比較的すばやく試せるのが魅力でした。

一方で Agent Framework は、Microsoft Learn の overview で説明されているように、AutoGen のシンプルな agent abstractions を引き継ぎつつ、より明示的な制御や状態管理を取り込みました。

初学者向けにざっくり整理すると、次の違いがあります。

- AutoGen
  - エージェント同士のやり取りを試しやすい
  - agent パターンの入口として分かりやすい

- Agent Framework
  - Agent に加えて Workflow を強く持つ
  - Session や Context Provider で状態を整理しやすい
  - 長めの実行や human-in-the-loop を見据えやすい

### 例
「複数のエージェントに自由に相談させたい」なら AutoGen 的な見方が理解しやすい場面があります。
一方で「要約して、レビューして、承認があれば次へ進む」のように順序や分岐を管理したいなら Agent Framework の Workflow のほうが考えやすいです。

要点:
- AutoGen は会話的な agent パターンの入口として分かりやすい
- Agent Framework はその先の制御や運用まで見据えやすい

## 15. Semantic Kernel と比べると何が違うか
Semantic Kernel は、AI 機能をアプリケーションに組み込むための SDK として広く使われてきました。

特に、
- plugins
- filters
- memory
- observability
- 型安全性

のような enterprise 向け要素が強いのが特徴です。

Agent Framework は、その系譜を引き継ぎながら、Agent と Workflow を中心に再整理した形として見ると分かりやすいです。

つまり、
- Semantic Kernel は「AI 機能を組み込む基盤」として捉えやすい
- Agent Framework は「agentic application を作る中心フレームワーク」として捉えやすい

要点:
- Semantic Kernel の強みだった enterprise 向け要素は、Agent Framework 側にも強く受け継がれている

## 16. どれを学べばよいか
2026-04-10 時点で新しく学ぶなら、この教材では Microsoft Agent Framework を先に学ぶことをおすすめします。

理由は 3 つです。

1. 2026-02-20 更新の overview で direct successor と明示されている
2. 2026-04-01 と 2026-04-02 に Semantic Kernel / AutoGen からの migration guide が公開されている
3. Agent と Workflow を同じ文脈で学べる

もちろん、既存コードベースが AutoGen や Semantic Kernel の場合は、そのまま読める知識も多いです。ですが、初学者が今から入口を選ぶなら、まず Agent Framework を主軸にすると整理しやすいです。

要点:
- 新規学習の主軸は Agent Framework
- 既存資産の理解には AutoGen / Semantic Kernel の知識も役立つ

## 17. よくあるつまずき
### つまずき 1
「Agent と Workflow の違いが曖昧」

対策:
会話の柔軟性を見るなら Agent、処理の順序を見るなら Workflow と覚える

### つまずき 2
「Session と Memory の違いが曖昧」

対策:
Session は会話の箱、Memory は持ち越したい情報の仕組みと分けて考える

### つまずき 3
「ツールを使う理由が分からない」

対策:
モデルの推測ではなく、外部の正しい情報を扱いたいときに使う

### つまずき 4
「AzureOpenAIChatClient で何を設定すればよいか分からない」

対策:
まずは `endpoint`、`api_key`、`deployment_name` の 3 つだけに絞って考える

### つまずき 5
「AutoGen と Semantic Kernel と Agent Framework の関係が分からない」

対策:
新規学習の中心を Agent Framework に置き、AutoGen は agent パターンの流れ、Semantic Kernel は enterprise SDK の流れとして整理する

## まとめ
- 最初は最小エージェントから始める
- Tools は外部の事実や機能につなぐ
- Session は会話をつなぎ、Memory は継続情報を管理する
- 手順を明示したいなら Workflow が向いている
- Azure OpenAI を使うときは `AzureOpenAIChatClient` に `endpoint` `api_key` `deployment_name` を渡す
- AutoGen と Semantic Kernel の強みを受け継いだ direct successor として見ると全体像をつかみやすい
