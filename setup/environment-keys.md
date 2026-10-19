# Environment Keys and Connectors

## Required
**Anthropic access.** Either log in with your Claude account, or set an API key:
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```
Never commit keys. `.gitignore` excludes `.env` files.

## Optional Connectors (via MCP)
Connect only what the client allows.

| Tool | Use |
|---|---|
| Google Drive or SharePoint | Read client documents and share outputs |
| Calendar | Plan SteerCo dates and check-ins |
| Slack or Teams | Draft and send team messages |
| Spreadsheets | Read data tables |
| Web search | Market and competitor research |

Run `/connect-mcps connect to [tool]` and log each connection in `outputs/mcp-integration-logs/`.

## Client Data Rule
Client data may only go through tools the client has approved in writing. If unsure, work on a local copy under the client's rules and ask the EM.
