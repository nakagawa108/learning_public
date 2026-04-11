# Microsoft Agent Framework 解答

## 演習の解答
### 演習 1
答え: B

理由:
Agent は入力を受けて考え、必要ならツールを使って応答する側だからです。A は Workflow の説明に近いです。

### 演習 2
答え: Session

理由:
前の会話内容を引き継いで 2 回目に答える必要があるためです。

### 演習 3
答えの例:
1. Tool を使うべき
2. 天気は外部の事実なので、モデルの推測ではなく外部データ取得で扱うほうが適切だから

### 演習 4
答え: Workflow

理由の例:
要約してからレビューするという処理順がはっきりしているためです。

### 演習 5
答えの例:
Session は、複数ターンの会話を 1 本の流れとして保つ箱です。  
Memory は、ユーザー情報や過去の文脈のような持ち越したい情報を管理する仕組みです。  
似ていますが、同じ役割ではありません。

### 演習 6
答えの例:
最小エージェント -> Tools -> Session -> Memory -> Workflow

理由の例:
まず 1 回答える最小構成を理解し、そのあとに機能を 1 つずつ足すと、何が増えたかを把握しやすいからです。

### 演習 7
答えの例:

```python
from agent_framework import AgentClient

# モデル用クライアントを作る
client = AgentClient(model="gpt-4.1-mini")

# 最小のエージェントを作る
agent = client.as_agent(
    name="study_helper",
    instructions="Python 学習の質問へ短く答えてください。"
)

# 1 回だけ実行する
result = agent.run("Python のリストとは？")
print(result)
```

ポイント:
- 最初は `クライアント作成 -> agent 作成 -> run` の流れが見えれば十分です
- 実際の import 名や初期化方法は、公式サンプルに合わせて調整してください

### 演習 8
答えの例:

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

ポイント:
- 大事なのは、Python の関数をツールとして agent に渡す考え方です
- 今回の `get_weather` はダミー実装でよく、まずは接続の形を理解します

### 演習 9
答えの例:

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

ポイント:
- 同じ `session` を渡し続けるのが重要です
- 2 回目だけ別 session にすると、会話がつながらない可能性があります

### 演習 10
答えの例:

```python
from agent_framework import AgentClient, Session

def get_weather(city: str) -> str:
    return f"{city} is sunny"

client = AgentClient(model="gpt-4.1-mini")

# Agent: ユーザー質問に答える本体
agent = client.as_agent(
    name="assistant_with_context",
    instructions="ユーザー情報を考慮しながら、必要ならツールを使って答えてください。",
    tools=[get_weather],
)

# Session: 複数ターン会話の箱
session = Session()

# Memory / context provider:
# 実際にはユーザー名や好みを context provider から注入する設計にする
user_context = {
    "user_name": "Aiko"
}

first = agent.run("東京の天気を教えて", session=session, context=user_context)
second = agent.run("私の名前も入れて答えて", session=session, context=user_context)

print(first)
print(second)
```

ポイント:
- Agent は返答役、Tool は外部機能、Session は会話維持、Memory は継続情報です
- 完全な API 一致より、部品の役割分担を理解して書けているかが大切です

### 演習 11
答えの例:

```python
import os
from agent_framework.azure import AzureOpenAIChatClient

chat_client = AzureOpenAIChatClient(
    endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
)

agent = chat_client.create_agent(
    instructions="Python 学習の質問へ短く答えてください。"
)

result = agent.run("Python のタプルとは？")
print(result)
```

ポイント:
- `AzureOpenAIChatClient` を作るときは、まず `endpoint` と `api_key` と `deployment_name` を見ると整理しやすいです
- 2025-10-09 の Microsoft Learn Quick Start では Azure CLI 資格情報を使う例に加え、API キー方式へ置き換え可能と案内されています

### 演習 12
答えの例:

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

ポイント:
- Azure OpenAI を使っていても、Tool は Python の関数として渡す考え方で学べます
- まずは接続先の設定と Tool 登録を分けて理解すると混乱しにくいです

## クイズの解答
### Q1
答え: Agent と Workflow

### Q2
答え: B

### Q3
答えの例:
複数ターンの会話で、前のやり取りを保ちながら返答したい場面です。

### Q4
答え: B

### Q5
答え: Workflow

### Q6
答えの例:
2026-02-20 更新の公式 overview では public preview と案内されているため、今後の変更を見込んで公式情報を確認しながら学ぶ必要がある点です。

### Q7
答え:
`Session` / `Memory`

## 最後の確認ポイント
- Agent は柔軟な実行主体
- Workflow は明示的な処理フロー
- Tool は外部機能や外部データにつなぐ
- Session と Memory は似ていても役割が違う
- Python 実装では、まず最小構成を書いてから Tool と Session を足すと理解しやすい
- Azure OpenAI 利用時は、Agent Framework の概念に加えて `endpoint` `api_key` `deployment_name` を整理する
