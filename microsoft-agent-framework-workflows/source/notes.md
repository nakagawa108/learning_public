# Microsoft Agent Framework Workflows 参照メモ

この教材は 2026-04-14 に作成した。  
Workflow 周辺は更新頻度が高いため、主に Microsoft Learn と Microsoft 公式 GitHub を参照して整理している。

## 主な参照元
- Agent Framework documentation  
  https://learn.microsoft.com/en-us/agent-framework/
- Microsoft Agent Framework repository  
  https://github.com/microsoft/agent-framework
- Microsoft Agent Framework Workflows - Using Workflows as Agents  
  https://learn.microsoft.com/en-us/agent-framework/user-guide/workflows/as-agents
- Microsoft Agent Framework Workflows - Human-in-the-loop  
  https://learn.microsoft.com/en-us/agent-framework/user-guide/workflows/orchestrations/human-in-the-loop
- Microsoft Agent Framework Workflows - Edges  
  https://learn.microsoft.com/en-us/agent-framework/workflows/edges

## 教材に反映したポイント
- Agent Framework の公式ドキュメントでは、`Agents` と `Workflows` が主要な学習軸として整理されている
- GitHub README では Workflows の特長として graph-based orchestration、streaming、checkpointing、human-in-the-loop、time-travel が挙げられている
- Edges には direct、conditional、switch-case、fan-out、fan-in などの代表パターンがある
- Workflow は単なる直列実行だけでなく、条件分岐や並列実行を設計しやすくするための仕組みとして扱われている
- Human-in-the-loop は途中停止して必要情報を人から受け取り、再開する流れとして学ぶ価値が高い

## 教材上の注意
- Python の細かい API シグネチャはリリースで変わりうるため、コード例は「考え方がわかる最小例」を優先した
- 実装時は Microsoft Learn の当日版サンプルも合わせて確認する
