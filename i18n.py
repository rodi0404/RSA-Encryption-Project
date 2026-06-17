"""
UI text and step templates for English/German bilingual support.
"""

LANGUAGES = {
    "en": "![GB](https://flagcdn.com/24x18/gb.png) EN",
    "de": "![DE](https://flagcdn.com/24x18/de.png) DE",
}

UI_TEXT = {
    "en": {
        "app_title": "🔐 Learning RSA Encryption",
        "github_button": "🔗 Github",
        "caption": "by Rodrigo Tomann",

        "tab_tutorial": "📚 Tutorial",
        "tab_generate": "🔑 Generate Keys",
        "tab_encrypt": "🔒 Encrypt",
        "tab_decrypt": "🔓 Decrypt",
        "tab_infos": "📖Infos",

        "tutorial_header": "📚 How to Use This App",
        "back": "← Back",
        "next": "Next →",
        "page_of": "Page {current} of {total}",
        "asymmetric_btn": "🔐 What is asymmetric encryption?",
        "back_to_tutorial": "← Back to Tutorial",
        "asymmetric_header": "🔐 What Is Asymmetric Encryption?",
        "asymmetric_image_caption": "Alice encrypts with Bob's public key, only Bob's private key can decrypt it",

        "gen_header": "Generate RSA Keys",
        "gen_subtitle": "Select key size and generate your public and private keys",
        "gen_radio_label": "Choose prime bit size:",
        "gen_bit_format": "{bits}-Bit Primes",
        "gen_button": "Generate Keys",
        "gen_spinner": "Generating keys...",
        "skip": "⏭️ Skip",
        "pause": "⏸️ Pause",
        "resume": "▶️ Resume",
        "paused": "⏸️ PAUSED",
        "next_step_in": "⏱️ Next step in {seconds}s",
        "keys_success": "✅ Keys Generated Successfully!",
        "public_key_box": "**Public Key (e, n)**\n\ne = {e}\n\nn = {n}",
        "private_key_box": "**Private Key (d, n)**\n\nd = {d}\n\nn = {n}",
        "verification_caption": "Verification: ({e} × {d}) mod {phi} = {result}",
        "complete_process": "📐 Complete Process (scroll down to see)",

        "encrypt_header": "Encrypt Message",
        "need_keys_warning": "⚠️ Generate keys first in the 'Generate Keys' tab",
        "encrypt_input_label": "Enter message to encrypt:",
        "encrypt_input_placeholder": "Type your message here",
        "public_key_settings": "**Public Key Settings:**",
        "use_custom_public_key": "Use custom public key (e, n)",
        "enter_e": "Enter e:",
        "enter_n": "Enter n:",
        "valid_keys": "✅ Valid keys: e = {e}, n = {n}",
        "using_generated_keys": "Using generated keys: e = {e}, n = {n}",
        "encryption_failed": "❌ Encryption failed: {error}",
        "encryption_breakdown": "📐 Step-by-Step Encryption Breakdown",
        "encryption_complete": "✅ Encryption Complete!",
        "original_label": "**Original:** {value}",
        "invalid_keys_error": "⚠️ Invalid keys. Please check the error messages above.",

        "decrypt_header": "Decrypt Message",
        "decrypt_input_label": "Enter encrypted numbers (as a list):",
        "decrypt_input_placeholder": "[123, 456, 789, ...]",
        "private_key_settings": "**Private Key Settings:**",
        "use_custom_private_key": "Use custom private key (d, n)",
        "enter_d": "Enter d:",
        "using_custom_keys_dn": "Using custom keys: d = {d}, n = {n}",
        "using_generated_keys_dn": "Using generated keys: d = {d}, n = {n}",
        "decryption_breakdown": "📐 Step-by-Step Decryption Breakdown",
        "decryption_complete": "✅ Decryption Complete!",
        "decryption_failed": "❌ Decryption failed: {error}",
        "decryption_failed_hint": "💡 Make sure you're using the correct private key (d, n) that matches the encryption key (e, n)",
        "input_must_be_list": "❌ Input must be a list of numbers",
        "parse_error": "❌ Error parsing input: {error}",
        "parse_error_hint": "Make sure to paste the encrypted numbers in the format: [123, 456, 789, ...]",

        "info_header": "How RSA Works",
        "info_basics_title": "🔑 The Basics",
        "info_math_title": "📐 How It Works Mathematically",
        "info_deterministic_title": "⚠️ Security Issue: Deterministic Encryption",
        "info_hybrid_title": "🔐 How Real Systems Fix This: Hybrid Encryption",
        "info_enhancements_title": "🛡️ Real-World Security Enhancements",

        "err_e_not_positive": "e must be a positive integer",
        "err_n_not_positive": "n must be a positive integer",
        "err_e_too_large": "e ({e}) must be less than n ({n})",
        "err_not_coprime": "e and n must be coprime (gcd(e, n) = 1). Currently gcd({e}, {n}) = {gcd}",
        "warn_n_small": "⚠️ n = {n} is very small. ASCII characters go up to 255, so encryption may fail or produce invalid characters.",
    },
    "de": {
        "app_title": "🔐 RSA-Verschlüsselung lernen",
        "github_button": "🔗 Github",
        "caption": "von Rodrigo Tomann",

        "tab_tutorial": "📚 Tutorial",
        "tab_generate": "🔑 Schlüssel erstellen",
        "tab_encrypt": "🔒 Verschlüsseln",
        "tab_decrypt": "🔓 Entschlüsseln",
        "tab_infos": "📖Infos",

        "tutorial_header": "📚 So benutzt du diese App",
        "back": "← Zurück",
        "next": "Weiter →",
        "page_of": "Seite {current} von {total}",
        "asymmetric_btn": "🔐 Was ist asymmetrische Verschlüsselung?",
        "back_to_tutorial": "← Zurück zum Tutorial",
        "asymmetric_header": "🔐 Was ist asymmetrische Verschlüsselung?",
        "asymmetric_image_caption": "Alice verschlüsselt mit Bobs öffentlichem Schlüssel, nur Bobs privater Schlüssel kann entschlüsseln",

        "gen_header": "RSA-Schlüssel erstellen",
        "gen_subtitle": "Wähle die Schlüsselgröße und erstelle deinen öffentlichen und privaten Schlüssel",
        "gen_radio_label": "Wähle die Bitgröße der Primzahlen:",
        "gen_bit_format": "{bits}-Bit-Primzahlen",
        "gen_button": "Schlüssel erstellen",
        "gen_spinner": "Schlüssel werden erstellt...",
        "skip": "⏭️ Überspringen",
        "pause": "⏸️ Pause",
        "resume": "▶️ Fortsetzen",
        "paused": "⏸️ PAUSIERT",
        "next_step_in": "⏱️ Nächster Schritt in {seconds}s",
        "keys_success": "✅ Schlüssel erfolgreich erstellt!",
        "public_key_box": "**Öffentlicher Schlüssel (e, n)**\n\ne = {e}\n\nn = {n}",
        "private_key_box": "**Privater Schlüssel (d, n)**\n\nd = {d}\n\nn = {n}",
        "verification_caption": "Überprüfung: ({e} × {d}) mod {phi} = {result}",
        "complete_process": "📐 Vollständiger Prozess (zum Anzeigen scrollen)",

        "encrypt_header": "Nachricht verschlüsseln",
        "need_keys_warning": "⚠️ Erstelle zuerst Schlüssel im Tab 'Schlüssel erstellen'",
        "encrypt_input_label": "Gib die zu verschlüsselnde Nachricht ein:",
        "encrypt_input_placeholder": "Gib hier deine Nachricht ein",
        "public_key_settings": "**Einstellungen für den öffentlichen Schlüssel:**",
        "use_custom_public_key": "Eigenen öffentlichen Schlüssel verwenden (e, n)",
        "enter_e": "Gib e ein:",
        "enter_n": "Gib n ein:",
        "valid_keys": "✅ Gültige Schlüssel: e = {e}, n = {n}",
        "using_generated_keys": "Verwende erstellte Schlüssel: e = {e}, n = {n}",
        "encryption_failed": "❌ Verschlüsselung fehlgeschlagen: {error}",
        "encryption_breakdown": "📐 Schritt-für-Schritt-Verschlüsselung",
        "encryption_complete": "✅ Verschlüsselung abgeschlossen!",
        "original_label": "**Original:** {value}",
        "invalid_keys_error": "⚠️ Ungültige Schlüssel. Bitte überprüfe die Fehlermeldungen oben.",

        "decrypt_header": "Nachricht entschlüsseln",
        "decrypt_input_label": "Gib die verschlüsselten Zahlen ein (als Liste):",
        "decrypt_input_placeholder": "[123, 456, 789, ...]",
        "private_key_settings": "**Einstellungen für den privaten Schlüssel:**",
        "use_custom_private_key": "Eigenen privaten Schlüssel verwenden (d, n)",
        "enter_d": "Gib d ein:",
        "using_custom_keys_dn": "Verwende eigene Schlüssel: d = {d}, n = {n}",
        "using_generated_keys_dn": "Verwende erstellte Schlüssel: d = {d}, n = {n}",
        "decryption_breakdown": "📐 Schritt-für-Schritt-Entschlüsselung",
        "decryption_complete": "✅ Entschlüsselung abgeschlossen!",
        "decryption_failed": "❌ Entschlüsselung fehlgeschlagen: {error}",
        "decryption_failed_hint": "💡 Stelle sicher, dass du den richtigen privaten Schlüssel (d, n) verwendest, der zum öffentlichen Schlüssel (e, n) passt",
        "input_must_be_list": "❌ Eingabe muss eine Liste von Zahlen sein",
        "parse_error": "❌ Fehler beim Verarbeiten der Eingabe: {error}",
        "parse_error_hint": "Stelle sicher, dass du die verschlüsselten Zahlen im Format [123, 456, 789, ...] einfügst",

        "info_header": "Wie RSA funktioniert",
        "info_basics_title": "🔑 Die Grundlagen",
        "info_math_title": "📐 Wie es mathematisch funktioniert",
        "info_deterministic_title": "⚠️ Sicherheitsproblem: Deterministische Verschlüsselung",
        "info_hybrid_title": "🔐 Wie echte Systeme das lösen: Hybride Verschlüsselung",
        "info_enhancements_title": "🛡️ Sicherheitsverbesserungen in der Praxis",

        "err_e_not_positive": "e muss eine positive ganze Zahl sein",
        "err_n_not_positive": "n muss eine positive ganze Zahl sein",
        "err_e_too_large": "e ({e}) muss kleiner als n ({n}) sein",
        "err_not_coprime": "e und n müssen teilerfremd sein (ggT(e, n) = 1). Aktuell ist ggT({e}, {n}) = {gcd}",
        "warn_n_small": "⚠️ n = {n} ist sehr klein. ASCII-Zeichen gehen bis 255, daher kann die Verschlüsselung fehlschlagen oder ungültige Zeichen erzeugen.",
    },
}


def t(lang, key, **kwargs):
    text = UI_TEXT[lang][key]
    return text.format(**kwargs) if kwargs else text


KEYGEN_STEP_TEMPLATES = {
    "en": [
        {
            "title": "**Step 1:** Generate prime p",
            "content": "**Formula:** p = random prime between 2^({bits}-1) and 2^{bits}\n\n**Range:** {low} to {high}\n\n**Result:** p = **{p}**",
        },
        {
            "title": "**Step 2:** Generate prime q",
            "content": "**Formula:** q = random prime between 2^({bits}-1) and 2^{bits}\n\n**Range:** {low} to {high}\n\n**Result:** q = **{q}**",
        },
        {
            "title": "**Step 3:** Calculate n (modulus)",
            "content": "**Formula:** n = p × q\n\n**Calculation:** n = {p} × {q}\n\n**Result:** n = **{n}**",
        },
        {
            "title": "**Step 4:** Calculate φ(n) - Euler's Totient",
            "content": "**Formula:** φ(n) = (p - 1) × (q - 1)\n\n**Calculation:** φ(n) = ({p} - 1) × ({q} - 1)\n\n**Calculation:** φ(n) = {p_minus_1} × {q_minus_1}\n\n**Result:** φ(n) = **{phi}**",
        },
        {
            "title": "**Step 5:** Choose public exponent e",
            "content": (
                "**Formula:** e = 65537 (standard choice)\n\n"
                "**What is GCD?**\n"
                "GCD (Greatest Common Divisor) is the largest number that divides both numbers evenly with no remainder.\n\n"
                "Example: gcd(12, 8) = 4 (since 4 divides both 12 and 8)\n\n"
                "**Why must gcd(e, φ(n)) = 1?**\n"
                "For RSA to work, e and φ(n) must be coprime (only share 1 as a common divisor). If they share other factors, we **can't** calculate the **private key d**.\n\n"
                "**Why use 65537?**\n"
                "- It's prime (only divisible by 1 and itself)\n"
                "- It's small (speeds up encryption)\n"
                "- It's almost always coprime with φ(n) (very rare exceptions)\n"
                "- It's the standard in cryptography (used by OpenSSL, TLS, etc.)\n"
                "- It's 10000000000000001 in binary\n\n"
                "**Verification:** gcd({e}, {phi}) = {gcd}\n\n"
                "**Result:** e = **{e}** ✅"
            ),
        },
        {
            "title": "**Step 6:** Calculate private exponent d",
            "content": (
                "**Formula:** d = e^(-1) mod φ(n) (modular multiplicative inverse)\n\n"
                "**Meaning:** Find d such that (e × d) mod φ(n) = 1\n\n"
                "**Calculation:** ({e} × d) mod {phi} = 1\n\n"
                "**Result:** d = **{d}**\n\n"
                "**Verification:** ({e} × {d}) mod {phi} = {verify}"
            ),
        },
    ],
    "de": [
        {
            "title": "**Schritt 1:** Primzahl p erzeugen",
            "content": "**Formel:** p = zufällige Primzahl zwischen 2^({bits}-1) und 2^{bits}\n\n**Bereich:** {low} bis {high}\n\n**Ergebnis:** p = **{p}**",
        },
        {
            "title": "**Schritt 2:** Primzahl q erzeugen",
            "content": "**Formel:** q = zufällige Primzahl zwischen 2^({bits}-1) und 2^{bits}\n\n**Bereich:** {low} bis {high}\n\n**Ergebnis:** q = **{q}**",
        },
        {
            "title": "**Schritt 3:** n berechnen (Modulus)",
            "content": "**Formel:** n = p × q\n\n**Berechnung:** n = {p} × {q}\n\n**Ergebnis:** n = **{n}**",
        },
        {
            "title": "**Schritt 4:** φ(n) berechnen – Eulersche Phi-Funktion",
            "content": "**Formel:** φ(n) = (p - 1) × (q - 1)\n\n**Berechnung:** φ(n) = ({p} - 1) × ({q} - 1)\n\n**Berechnung:** φ(n) = {p_minus_1} × {q_minus_1}\n\n**Ergebnis:** φ(n) = **{phi}**",
        },
        {
            "title": "**Schritt 5:** Öffentlichen Exponenten e wählen",
            "content": (
                "**Formel:** e = 65537 (Standardwahl)\n\n"
                "**Was ist der ggT?**\n"
                "Der ggT (größter gemeinsamer Teiler) ist die größte Zahl, die beide Zahlen ohne Rest teilt.\n\n"
                "Beispiel: ggT(12, 8) = 4 (da 4 sowohl 12 als auch 8 teilt)\n\n"
                "**Warum muss ggT(e, φ(n)) = 1 sein?**\n"
                "Damit RSA funktioniert, müssen e und φ(n) teilerfremd sein (nur 1 als gemeinsamen Teiler haben). Teilen sie sich andere Faktoren, können wir den **privaten Schlüssel d** **nicht** berechnen.\n\n"
                "**Warum 65537 verwenden?**\n"
                "- Es ist eine Primzahl (nur durch 1 und sich selbst teilbar)\n"
                "- Es ist klein (beschleunigt die Verschlüsselung)\n"
                "- Es ist fast immer teilerfremd zu φ(n) (sehr seltene Ausnahmen)\n"
                "- Es ist der Standard in der Kryptografie (verwendet von OpenSSL, TLS, usw.)\n"
                "- Es ist 10000000000000001 im Binärsystem\n\n"
                "**Überprüfung:** ggT({e}, {phi}) = {gcd}\n\n"
                "**Ergebnis:** e = **{e}** ✅"
            ),
        },
        {
            "title": "**Schritt 6:** Privaten Exponenten d berechnen",
            "content": (
                "**Formel:** d = e^(-1) mod φ(n) (modulares multiplikatives Inverses)\n\n"
                "**Bedeutung:** Finde d, sodass (e × d) mod φ(n) = 1\n\n"
                "**Berechnung:** ({e} × d) mod {phi} = 1\n\n"
                "**Ergebnis:** d = **{d}**\n\n"
                "**Überprüfung:** ({e} × {d}) mod {phi} = {verify}"
            ),
        },
    ],
}

ENCRYPT_STEP_TEMPLATES = {
    "en": [
        {
            "title": "**Step 1:** Convert message to characters",
            "content": "**Formula:** message → [char₁, char₂, ..., charₙ]\n\n**Original message:** \"{message}\"\n\n**Characters:** {chars}",
        },
        {
            "title": "**Step 2:** Convert each character to ASCII value",
            "content": "**Formula:** char → ord(char)\n\n**Conversions:** {ascii_display}\n\n**ASCII values:** {ascii_values}\n\n📚 [Learn more about ASCII codes](https://www.ascii-code.com)",
        },
        {
            "title": "**Step 3:** Encrypt each ASCII value",
            "content": "**Formula:** encrypted = ASCII^e mod n\n\nWhere e = {e}, n = {n}\n\n**Calculations:**\n\n{calculations}",
        },
        {
            "title": "**Step 4:** Collect into encrypted list",
            "content": "**Result:** All encrypted values combined into one list\n\n**Encrypted message:** {encrypted}\n\nEach number represents one character from your original message!",
        },
    ],
    "de": [
        {
            "title": "**Schritt 1:** Nachricht in Zeichen umwandeln",
            "content": "**Formel:** Nachricht → [Zeichen₁, Zeichen₂, ..., Zeichenₙ]\n\n**Originalnachricht:** \"{message}\"\n\n**Zeichen:** {chars}",
        },
        {
            "title": "**Schritt 2:** Jedes Zeichen in ASCII-Wert umwandeln",
            "content": "**Formel:** Zeichen → ord(Zeichen)\n\n**Umwandlungen:** {ascii_display}\n\n**ASCII-Werte:** {ascii_values}\n\n📚 [Mehr über ASCII-Codes erfahren](https://www.ascii-code.com)",
        },
        {
            "title": "**Schritt 3:** Jeden ASCII-Wert verschlüsseln",
            "content": "**Formel:** verschlüsselt = ASCII^e mod n\n\nWobei e = {e}, n = {n}\n\n**Berechnungen:**\n\n{calculations}",
        },
        {
            "title": "**Schritt 4:** In verschlüsselte Liste sammeln",
            "content": "**Ergebnis:** Alle verschlüsselten Werte werden in einer Liste zusammengefasst\n\n**Verschlüsselte Nachricht:** {encrypted}\n\nJede Zahl steht für ein Zeichen aus deiner Originalnachricht!",
        },
    ],
}

DECRYPT_STEP_TEMPLATES = {
    "en": [
        {
            "title": "**Step 1:** Encrypted list received",
            "content": "**Encrypted numbers:** {encrypted_list}\n\nEach number represents one encrypted character.",
        },
        {
            "title": "**Step 2:** Decrypt each number",
            "content": "**Formula:** ASCII = encrypted^d mod n\n\nWhere d = {d}, n = {n}\n\n**Calculations:**\n\n{calculations}",
        },
        {
            "title": "**Step 3:** Convert ASCII to characters",
            "content": "**Formula:** ASCII → chr(ASCII)\n\n**Conversions:** {conversions}\n\n📚 [Learn more about ASCII codes](https://www.ascii-code.com)",
        },
        {
            "title": "**Step 4:** Combine into message",
            "content": "**Result:** All characters combined into final message\n\n**Decrypted message:** \"{decrypted}\"",
        },
    ],
    "de": [
        {
            "title": "**Schritt 1:** Verschlüsselte Liste empfangen",
            "content": "**Verschlüsselte Zahlen:** {encrypted_list}\n\nJede Zahl steht für ein verschlüsseltes Zeichen.",
        },
        {
            "title": "**Schritt 2:** Jede Zahl entschlüsseln",
            "content": "**Formel:** ASCII = verschlüsselt^d mod n\n\nWobei d = {d}, n = {n}\n\n**Berechnungen:**\n\n{calculations}",
        },
        {
            "title": "**Schritt 3:** ASCII in Zeichen umwandeln",
            "content": "**Formel:** ASCII → chr(ASCII)\n\n**Umwandlungen:** {conversions}\n\n📚 [Mehr über ASCII-Codes erfahren](https://www.ascii-code.com)",
        },
        {
            "title": "**Schritt 4:** Zur Nachricht zusammensetzen",
            "content": "**Ergebnis:** Alle Zeichen werden zur endgültigen Nachricht zusammengesetzt\n\n**Entschlüsselte Nachricht:** \"{decrypted}\"",
        },
    ],
}
