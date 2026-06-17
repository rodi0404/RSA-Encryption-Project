# Code Conventions & RSA Invariants (app.py)

- This is intentionally *textbook* RSA for teaching: no padding (OAEP etc.), deterministic ciphertext, small key sizes (8/16/128-bit). Do not "fix" these as bugs — they're documented limitations (see README "Limitations & Security Notes").
- `chooseE(phi, bit_size)` picks `e` from a hardcoded candidate list that depends on `bit_size` (8-bit: `[5,17,257]`; 16-bit: `[17,257,65537]`; else: `[65537,257,17,5,3]`), filtering for `e < phi and gcd(e, phi) == 1`. Raises `ValueError` if none work. Any new bit-size tier must extend this table.
- `validate_public_key(e, n)` is the canonical check for custom/user-supplied keys: requires positive ints, `e < n`, `gcd(e, n) == 1`, and warns (not errors) if `n < 256` since ASCII chars go up to 255 — message encryption silently breaks below that without an explicit error.
- Per README: cryptographic/math code is hand-written by the author; AI was used only for educational copy in `content.py`. Keep that separation when making changes — don't let AI-authored prose drift into the RSA math functions' logic.
