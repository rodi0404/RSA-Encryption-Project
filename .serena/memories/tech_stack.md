# Tech Stack

- Python 3 (Streamlit `>=1.28.0`, SymPy `>=1.12` — see `requirements.txt`; no lockfile, no pinned exact versions).
- No build step. Single-file Streamlit app, run directly with the `streamlit` CLI.
- No test suite, no linter/formatter config present in the repo.
- MCP: Serena is configured project-locally in `.mcp.json` (runs via `uvx --from git+https://github.com/oraios/serena`); requires `uv`/`uvx` on PATH (installed under `C:\Users\<user>\.local\bin` on this machine, not on PATH for already-open shells until restarted).
