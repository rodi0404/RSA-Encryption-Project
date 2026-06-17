# Suggested Commands (Windows)

- Run app: `streamlit run app.py` (opens at http://localhost:8501).
- Install deps: `pip install -r requirements.txt`.
- Shell in this environment: Bash tool here is Git Bash (POSIX paths like `/e/coding/...`), but the user's own terminal is `cmd.exe`/PowerShell with native Windows paths (`E:\coding\...`) — don't mix path styles when suggesting commands to the user.
- `uvx`/`uv`/`serena` only resolve in shells opened after the uv installer ran; a cmd.exe window opened earlier needs to be closed and reopened to pick up the updated PATH.
