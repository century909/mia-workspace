---
name: google-sheets-mcp
description: Manage Google Sheets and Drive files using an MCP server.
metadata: {"openclaw":{"emoji":"📊"}}
---

# Google Sheets MCP

This skill provides a bridge to your local Google Sheets MCP server.

## Configuration
- Path: `/home/diego/Documentos/telegrammcp/proyectostdiooauth/mcp-google-sheets`
- Credentials: `/home/diego/Documentos/telegrammcp/proyectostdiooauth/credentials.json`
- Token: `/home/diego/Documentos/telegrammcp/proyectostdiooauth/token_7093642367.json`

## Commands
Use `npx mcporter call` with the following tools:
- `list_spreadsheets()`: List all spreadsheets.
- `create_spreadsheet(title)`: Create a new spreadsheet.
- `read_spreadsheet(spreadsheet_id, range_name)`: Read data.
- `write_to_spreadsheet(spreadsheet_id, range_name, values)`: Write data.
- `append_to_spreadsheet(spreadsheet_id, range_name, values)`: Append data.
- `get_spreadsheet_info(spreadsheet_id)`: Get metadata.
- `create_sheet(spreadsheet_id, sheet_name)`: Create a sheet.
- `delete_sheet(spreadsheet_id, sheet_id)`: Delete a sheet.

## Usage
Always export the required environment variables before calling:
```bash
export CREDENTIALS_PATH='/home/diego/Documentos/telegrammcp/proyectostdiooauth/credentials.json'
export TOKEN_PATH='/home/diego/Documentos/telegrammcp/proyectostdiooauth/token_7093642367.json'
npx mcporter call --stdio "/bin/bash -c 'cd /home/diego/Documentos/telegrammcp/proyectostdiooauth/mcp-google-sheets && /home/diego/Documentos/telegrammcp/proyectostdiooauth/venv/bin/python3 -m src.mcp_google_sheets.server'" <tool_name> <args>
```
