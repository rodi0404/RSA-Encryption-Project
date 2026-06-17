# RSA Encryption Project — Core Map

Single-module Streamlit educational app demonstrating textbook RSA. No package structure, no tests, no CI.

- `app.py` — the live app (run via `streamlit run app.py`). Contains all RSA math (`calculatepq`, `chooseE`, `calculateD`, `encrypt`, `decrypt`, `validate_public_key`) plus the entire Streamlit UI (tabs, animated step-by-step reveals, custom-key testing) in one file.
- `content.py` — static educational text only (`get_tutorial_steps`, `get_info_content`), no logic. Edit here for copy changes, not `app.py`.
- `oldmain.py`, `poc.py` — superseded/reference RSA implementations, not imported by `app.py`. Treat as historical reference only; do not extend them.

See `mem:tech_stack`, `mem:conventions`, `mem:suggested_commands`, `mem:task_completion` for details.

For RSA-math invariants specific to this codebase (key-size-dependent `e` selection, validation rules), see `mem:conventions`.
