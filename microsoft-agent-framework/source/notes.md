# Microsoft Agent Framework 参照メモ

この教材は 2026-04-10 に初版を作成した。
内容は主に Microsoft Learn と Microsoft の公式 GitHub リポジトリをもとに整理している。

## 主要参照
- Microsoft Agent Framework Overview  
  https://learn.microsoft.com/en-us/agent-framework/overview/
- Get started with Agent Framework  
  https://learn.microsoft.com/en-us/agent-framework/get-started/
- Step 1: Your First Agent  
  https://learn.microsoft.com/en-us/agent-framework/tutorials/overview
- Step 2: Add Tools  
  https://learn.microsoft.com/en-us/agent-framework/get-started/add-tools
- Step 4: Memory & Persistence  
  https://learn.microsoft.com/en-us/agent-framework/get-started/memory
- Workflows Overview  
  https://learn.microsoft.com/en-us/agent-framework/workflows/
- Workflow Builder & Execution  
  https://learn.microsoft.com/en-us/agent-framework/user-guide/workflows/core-concepts/workflows
- FAQ  
  https://learn.microsoft.com/en-us/agent-framework/support/faq
- Microsoft Agent Framework Quick Start  
  https://learn.microsoft.com/en-us/agent-framework/tutorials/quick-start?pivots=programming-language-python
- GitHub Repository  
  https://github.com/microsoft/agent-framework
- Migration Guide Overview  
  https://learn.microsoft.com/en-us/agent-framework/migration-guide/
- Migration Guide from AutoGen  
  https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/
- Migration Guide from Semantic Kernel  
  https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel/

## 教材に反映したポイント
- Agent Framework は Microsoft Learn 上で公開されている現行のエージェント開発フレームワークである
- 主な軸は `Agents` と `Workflows`
- チュートリアルは Step 1 から Step 6 まで段階的に進む
- 公式 FAQ では .NET と Python がサポート対象として案内されている
- 2026-02-20 更新の overview では public preview とされている
- 2025-12-08 更新の quick start では Python 側に `AzureAIClient` の例がある
- GitHub 上の Python 例や issue 再現コードでは `agent_framework.azure.AzureOpenAIChatClient` の利用例も確認できる
- 2025-10-09 の Quick Start では Azure CLI 資格情報の例に加えて、API キー方式へ置き換え可能と案内されている

## ローカル教材サンプル
- `source/azure_openai_chat_client_sample.py`
  - `AzureOpenAIChatClient`
  - `api_key`
  - Tool 登録
  - 2 回の実行例
