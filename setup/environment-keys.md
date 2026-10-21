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
| Google Drive | Read, create, convert, copy, and share files. Creates Google Sheets from CSV in one call |
| Google Sheets editor | Build and edit models and trackers in place |
| Google Slides editor | Build and edit decks in place, with linked Sheets charts |
| Google Docs editor | Memos and write-ups |
| SharePoint | Read client documents and share outputs |
| Calendar | Plan SteerCo dates and check-ins |
| Slack or Teams | Draft and send team messages |
| Spreadsheets | Read data tables |
| Web search | Market and competitor research |

Run `/connect-mcps connect to [tool]` and log each connection in `outputs/mcp-integration-logs/`.

## Client Data Rule
Client data may only go through tools the client has approved in writing. If unsure, work on a local copy under the client's rules and ask the EM.
