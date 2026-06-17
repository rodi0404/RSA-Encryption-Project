# Task Completion Checklist

No automated linter, formatter, or test suite exists in this repo. To consider a coding task done:
1. Manually run `streamlit run app.py` and exercise the affected tab (Tutorial/Generate Keys/Encrypt/Decrypt/Info) in a browser at localhost:8501.
2. For changes to RSA math functions, sanity-check with a small custom key pair via the "use custom keys" option in the Encrypt/Decrypt tabs to confirm round-trip correctness.
3. No CI to satisfy — there is none configured.
