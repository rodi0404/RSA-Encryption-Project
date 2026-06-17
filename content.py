"""
Content strings and data structures for the RSA Encryption Tool.
This file contains all the tutorial steps, info content, and educational text.
"""

def get_tutorial_steps(lang="en"):
    """Returns the tutorial steps for the "How to Use This App" section."""
    if lang == "de":
        return [
            {
                "title": "Willkommen bei RSA-Verschlüsselung",
                "content": """
                Willkommen! Diese App zeigt dir Schritt für Schritt, wie **RSA-Verschlüsselung** funktioniert.

                RSA wird in echten Anwendungen verwendet, wie zum Beispiel:
                - 🔒 HTTPS-Webseiten
                - 📧 E-Mail-Verschlüsselung
                - 💳 Digitale Signaturen
                - 🔐 Sichere Messaging-Apps

                Lass uns gemeinsam lernen, wie es funktioniert!
                """,
                "emoji": "👋"
            },
            {
                "title": "Bevor du startest",
                "content": """
                **Diese App setzt voraus, dass du die Grundlagen der asymmetrischen Verschlüsselung verstehst:**

                - ✅ Was öffentliche Schlüssel sind (können mit jedem geteilt werden)
                - ✅ Was private Schlüssel sind (müssen geheim bleiben)
                - ✅ Wie öffentliche Schlüssel Nachrichten verschlüsseln
                - ✅ Wie private Schlüssel Nachrichten entschlüsseln
                - ✅ Warum man mit dem falschen Schlüssel nicht entschlüsseln kann

                **Falls dir diese Konzepte neu sind,** hilft es, vorher ein grundlegendes Verständnis zu haben. Diese App ist aber dafür gemacht, dir zu zeigen, *wie* RSA mathematisch genau funktioniert!

                Bereit? Los geht's! 🚀
                """,
                "emoji": "⚠️"
            },
            {
                "title": "Schritt 1: Schlüssel erstellen",
                "content": """
                **Was passiert:** Die App erstellt einen öffentlichen Schlüssel (e, n) und einen privaten Schlüssel (d, n).

                1. Gehe zum Tab "🔑 Schlüssel erstellen"
                2. Wähle eine Bitgröße für die Primzahlen (8, 16 oder 128 Bit)
                3. Klicke auf "Schlüssel erstellen"
                4. Schau dir den animierten Schritt-für-Schritt-Prozess an!

                **Warum das wichtig ist:**
                - Öffentlicher Schlüssel = Mit jedem teilbar (wie deine E-Mail-Adresse)
                - Privater Schlüssel = Geheim halten! (wie dein Passwort)
                """,
                "emoji": "🔑"
            },
            {
                "title": "Schritt 2: Eine Nachricht verschlüsseln",
                "content": """
                **Was passiert:** Deine Nachricht wird mit dem öffentlichen Schlüssel in Zahlen umgewandelt.

                1. Gehe zum Tab "🔒 Verschlüsseln"
                2. Tippe deine Nachricht ein (z. B. "Hallo")
                3. Die App verschlüsselt sie mit den erstellten Schlüsseln
                4. Du erhältst verschlüsselte Zahlen, die wie Kauderwelsch aussehen!

                **Optional:** Verwende eigene öffentliche Schlüssel, um mit anderen Schlüsseln zu testen.
                """,
                "emoji": "🔒"
            },
            {
                "title": "Schritt 3: Eine Nachricht entschlüsseln",
                "content": """
                **Was passiert:** Die verschlüsselten Zahlen werden mit dem privaten Schlüssel zurück in lesbaren Text umgewandelt.

                1. Gehe zum Tab "🔓 Entschlüsseln"
                2. Füge die verschlüsselten Zahlen ein (die aus der Verschlüsselung)
                3. Die App entschlüsselt sie mit dem passenden privaten Schlüssel
                4. Du erhältst deine Originalnachricht zurück!

                **Wichtig:** Du kannst NUR mit dem passenden privaten Schlüssel entschlüsseln. Der falsche Schlüssel liefert Kauderwelsch.
                """,
                "emoji": "🔓"
            },
            {
                "title": "Testen mit eigenen Schlüsseln",
                "content": """
                **Fortgeschrittene Funktion:** Du kannst RSA mit deinen eigenen Schlüsseln testen!

                1. **Verschlüsseln-Tab:** Aktiviere "Eigenen öffentlichen Schlüssel verwenden" und gib e und n ein
                2. **Entschlüsseln-Tab:** Aktiviere "Eigenen privaten Schlüssel verwenden" und gib d und n ein

                **Probiere das:**
                - Verschlüssele mit einem öffentlichen Schlüssel (e₁, n)
                - Versuche, mit einem ANDEREN privaten Schlüssel (d₂, n) zu entschlüsseln
                - Sieh, dass es nur Kauderwelsch ergibt! ✓ Das beweist, dass die Sicherheit funktioniert.

                Nur der passende private Schlüssel kann entschlüsseln!
                """,
                "emoji": "🧪"
            },
            {
                "title": "Wichtige Erkenntnisse",
                "content": """
                **Warum RSA sicher ist:**
                - ✅ Jeder kann mit dem öffentlichen Schlüssel verschlüsseln
                - ✅ Nur du kannst mit dem privaten Schlüssel entschlüsseln
                - ✅ Selbst wenn jemand e und n kennt, kann er d nicht berechnen
                - ✅ Es zu brechen würde die Faktorisierung von n erfordern (extrem schwer!)

                **Die Schlüsselgröße ist wichtig:**
                - 8-Bit: Nur zur Veranschaulichung (leicht zu brechen)
                - 16-Bit: Immer noch klein (zum Lernen)
                - 128-Bit: Viel stärker (aber immer noch nicht produktionsreif)
                - Echte Systeme: 2048-4096 Bit
                """,
                "emoji": "💡"
            },
            {
                "title": "Bereit zum Erkunden!",
                "content": """
                Du bist bereit! Hier ist, was du ausprobieren kannst:

                1. **Schlüssel erstellen** - Beobachte die Mathematik in Echtzeit
                2. **Verschlüsseln** - Tippe eine geheime Nachricht ein und sieh, wie sie verschlüsselt wird
                3. **Entschlüsseln** - Entschlüssele sie zurück und überprüfe, ob sie übereinstimmt
                4. **Experimentieren** - Probiere eigene Schlüssel aus und schau, was kaputt geht!
                5. **Lernen** - Schau im Tab "📖Infos" für tiefere Erklärungen vorbei

                **Viel Spaß beim Erkunden der Kryptografie!** 🚀
                """,
                "emoji": "🚀"
            }
        ]

    return [
        {
            "title": "Welcome to RSA Encryption",
            "content": """
            Welcome! This app teaches you how **RSA encryption** works step by step.

            RSA is the encryption used in real-world applications like:
            - 🔒 HTTPS websites
            - 📧 Email encryption
            - 💳 Digital signatures
            - 🔐 Secure messaging apps

            Let's learn how it works together!
            """,
            "emoji": "👋"
        },
        {
            "title": "Before You Start",
            "content": """
            **This app assumes you understand the basics of asymmetric encryption:**

            - ✅ What public keys are (can be shared with anyone)
            - ✅ What private keys are (must be kept secret)
            - ✅ How public keys encrypt messages
            - ✅ How private keys decrypt messages
            - ✅ Why you can't decrypt with the wrong key

            **If you're new to these concepts,** it's helpful to have a basic understanding before diving in. However, this app is designed to teach you *how* RSA specifically works mathematically!

            Ready? Let's go! 🚀
            """,
            "emoji": "⚠️"
        },
        {
            "title": "Step 1: Generate Keys",
            "content": """
            **What happens:** The app generates a public key (e, n) and private key (d, n).

            1. Go to the "🔑 Generate Keys" tab
            2. Choose a prime bit size (8, 16, or 128 bit)
            3. Click "Generate Keys"
            4. Watch the animated step-by-step process!

            **Why it matters:**
            - Public key = Share with anyone (like your email address)
            - Private key = Keep secret! (like your password)
            """,
            "emoji": "🔑"
        },
        {
            "title": "Step 2: Encrypt a Message",
            "content": """
            **What happens:** Your message gets transformed into numbers using the public key.

            1. Go to the "🔒 Encrypt" tab
            2. Type your message (e.g., "Hello")
            3. The app encrypts it with the generated keys
            4. You get encrypted numbers that look like gibberish!

            **Optional:** Use custom public keys to test with different keys.
            """,
            "emoji": "🔒"
        },
        {
            "title": "Step 3: Decrypt a Message",
            "content": """
            **What happens:** The encrypted numbers get transformed back into readable text using the private key.

            1. Go to the "🔓 Decrypt" tab
            2. Paste the encrypted numbers (the ones from encryption)
            3. The app decrypts them with the matching private key
            4. You get your original message back!

            **Important:** You can ONLY decrypt with the matching private key. Using the wrong key gives gibberish.
            """,
            "emoji": "🔓"
        },
        {
            "title": "Testing with Custom Keys",
            "content": """
            **Advanced feature:** You can test RSA with your own keys!

            1. **Encrypt tab:** Check "Use custom public key" and enter e and n
            2. **Decrypt tab:** Check "Use custom private key" and enter d and n

            **Try this:**
            - Encrypt with one public key (e₁, n)
            - Try to decrypt with a DIFFERENT private key (d₂, n)
            - See that it gives garbage! ✓ This proves the security works.

            Only the matching private key can decrypt!
            """,
            "emoji": "🧪"
        },
        {
            "title": "Key Insights",
            "content": """
            **Why RSA is secure:**
            - ✅ Anyone can encrypt with the public key
            - ✅ Only you can decrypt with the private key
            - ✅ Even if someone knows e and n, they can't calculate d
            - ✅ Breaking it would require factoring n (extremely hard!)

            **Key size matters:**
            - 8-bit: Educational only (easy to break)
            - 16-bit: Still small (learning purposes)
            - 128-bit: Much stronger (but still not production-grade)
            - Real systems: 2048-4096 bit
            """,
            "emoji": "💡"
        },
        {
            "title": "Ready to Explore!",
            "content": """
            You're all set! Here's what to try:

            1. **Generate Keys** - Watch the math happen in real-time
            2. **Encrypt** - Type a secret message and see it encrypted
            3. **Decrypt** - Decrypt it back and verify it matches
            4. **Experiment** - Try custom keys and see what breaks!
            5. **Learn** - Check the "📖Infos" tab for deeper explanations

            **Have fun exploring cryptography!** 🚀
            """,
            "emoji": "🚀"
        }
    ]


def get_asymmetric_explanation_intro(lang="en"):
    """Returns the analogy and motivation part of the asymmetric encryption explanation."""
    if lang == "de":
        return """
        **Stell dir einen Briefkasten mit einem besonderen Schloss vor:**

        - 📬 Jeder kann einen Brief durch den Schlitz in den Briefkasten einwerfen (der **öffentliche Schlüssel**)
        - 🔑 Aber nur der Besitzer hat den Schlüssel, um den Briefkasten zu öffnen und die Briefe zu lesen (der **private Schlüssel**)

        Das ist die Grundidee der asymmetrischen Verschlüsselung! Anders als bei einem normalen Schloss, bei dem derselbe Schlüssel auf- und zuschließt, hat man hier **zwei verschiedene Schlüssel**:

        - **Öffentlicher Schlüssel** — verschließt (verschlüsselt) die Nachricht. Kann sicher an jeden weitergegeben werden, sogar an Feinde.
        - **Privater Schlüssel** — öffnet (entschlüsselt) die Nachricht. Niemals mit jemandem teilen.

        **Warum zwei Schlüssel statt einem?**

        Bei einem einzigen gemeinsamen Schlüssel (symmetrische Verschlüsselung) brauchen beide Personen den *gleichen* geheimen Schlüssel — der also irgendwie ausgetauscht werden muss, und jeder, der ihn abfängt, kann alles mitlesen. Asymmetrische Verschlüsselung löst das: Du kannst deinen öffentlichen Schlüssel der ganzen Welt zeigen, und Leute können dir Geheimnisse schicken, die **nur du** lesen kannst, ohne vorher heimlich einen Schlüssel austauschen zu müssen.

        **Ein einfacher Ablauf aus der echten Welt:**
        """

    return """
    **Imagine a mailbox with a special lock:**

    - 📬 Anyone can drop a letter into the mailbox through the slot (the **public key**)
    - 🔑 But only the owner has the key to open the mailbox and read the letters (the **private key**)

    That's the core idea behind asymmetric encryption! Unlike a normal lock where the same key locks and unlocks, here you have **two different keys**:

    - **Public key** — locks (encrypts) the message. Safe to give to anyone, even your enemies.
    - **Private key** — unlocks (decrypts) the message. Never share this with anyone.

    **Why two keys instead of one?**

    With a single shared key (symmetric encryption), both people need the *same* secret key — which means it has to be exchanged somehow, and anyone who intercepts it can read everything. Asymmetric encryption solves this: you can publish your public key to the entire world, and people can send you secrets that **only you** can read, without ever needing to secretly share a key first.

    **A simple real-world flow:**
    """


def get_asymmetric_explanation_outro(lang="en"):
    """Returns the wrap-up part of the asymmetric encryption explanation, shown after the diagram."""
    if lang == "de":
        return """
        1. Bob teilt seinen **öffentlichen Schlüssel** mit jedem, auch mit Alice
        2. Alice nimmt ihre Nachricht, **"Ruf mich heute an"**, und verschlüsselt sie mit Bobs öffentlichem Schlüssel zu Kauderwelsch: **"dh12#djdi2+rg"**
        3. Alice schickt das Kauderwelsch an Bob — fängt es jemand ab, ist es unlesbar
        4. Bob entschlüsselt das Kauderwelsch mit seinem **privaten Schlüssel** zurück zu **"Ruf mich heute an"**

        Nur Bobs privater Schlüssel kann umkehren, was Bobs öffentlicher Schlüssel verschlüsselt hat — deshalb kann jeder seinen öffentlichen Schlüssel sicher verwenden, aber nur er kann das Ergebnis lesen.

        Genau das macht RSA — nur dass statt eines physischen Briefkastens Mathematik diesen "Schloss"- und "Schlüssel"-Effekt erzeugt. Der Rest dieses Tutorials zeigt dir genau, wie!
        """

    return """
    1. Bob shares his **public key** with anyone, including Alice
    2. Alice takes her message, **"Call me today"**, and combines it with Bob's public key to encrypt it into gibberish: **"dh12#djdi2+rg"**
    3. Alice sends that gibberish to Bob — if anyone intercepts it, it's unreadable
    4. Bob combines the gibberish with his **private key** to decrypt it back into **"Call me today"**

    Only Bob's private key can undo what Bob's public key encrypted — that's why anyone can safely use his public key, but only he can read the result.

    This is exactly what RSA does — except instead of a physical mailbox, it uses math to create that "lock" and "key" effect. The rest of this tutorial will show you exactly how!
    """


def get_info_content(lang="en"):
    """Returns the content for the 'How RSA Works' info tab."""
    if lang == "de":
        return {
            "basics": """
            **RSA (Rivest-Shamir-Adleman)** ist ein asymmetrischer Verschlüsselungsalgorithmus, der zwei Schlüssel verwendet:

            - **Öffentlicher Schlüssel (e, n)**: Kann mit jedem geteilt werden. Wird zum Verschlüsseln von Nachrichten verwendet.
            - **Privater Schlüssel (d, n)**: Bleibt geheim. Wird zum Entschlüsseln von Nachrichten verwendet.

            Die Magie: Etwas, das mit dem öffentlichen Schlüssel verschlüsselt wurde, kann NUR mit dem privaten Schlüssel entschlüsselt werden.
            """,
            "mathematics": """
            1. **Erzeuge zwei große Primzahlen** (p und q)
            2. **Berechne n** = p × q (der Modulus, in beiden Schlüsseln enthalten)
            3. **Berechne φ(n)** = (p-1) × (q-1) (Eulersche Phi-Funktion)
            4. **Wähle e** (öffentlicher Exponent) = meist 65537 (muss teilerfremd zu φ sein)
            5. **Berechne d** (privater Exponent) = das modulare Inverse von e (mod φ)

            **Verschlüsselung:** Geheimtext = Nachricht^e mod n

            **Entschlüsselung:** Nachricht = Geheimtext^d mod n
            """,
            "deterministic_issue": """
            **Das Problem:** In dieser einfachen Implementierung verschlüsselt sich dasselbe Zeichen immer zur selben Zahl.

            Beispiel: "hallo" wird immer zu [542, 189, 203, 203, 445]

            Ein Angreifer kann mit Häufigkeitsanalyse erraten, welche Buchstaben du verschlüsselst!
            """,
            "hybrid_solution": """
            **Echte Verschlüsselungssoftware (wie GPG, PGP, Signal) verwendet hybride Verschlüsselung:**

            1. **Erzeuge einen zufälligen symmetrischen Schlüssel** (256-Bit-AES-Schlüssel)
            2. **Verschlüssele deine eigentliche Nachricht** mit dem AES-Schlüssel (schnell, und jede Verschlüsselung ist anders!)
            3. **Verschlüssele den AES-Schlüssel** mit RSA (nur den 256-Bit-Schlüssel, nicht die ganze Nachricht)
            4. **Sende beides:** verschlüsselte Nachricht + verschlüsselter Schlüssel

            **Vorteile:**
            - ✅ Jede Verschlüsselung ist anders (auch für dieselbe Nachricht)
            - ✅ RSA verschlüsselt nur einen kleinen Schlüssel (schnell)
            - ✅ AES-Verschlüsselung ist sehr schnell
            - ✅ Sicher gegen Häufigkeitsanalyse

            **Warum nicht einfach nur RSA verwenden?**
            - RSA ist langsam (besonders bei großen Schlüsseln)
            - RSA kann nur kleine Datenmengen verschlüsseln
            - Rohes RSA ist anfällig für Angriffe

            Deshalb verwenden PGP/GPG/Signal alle diesen hybriden Ansatz!
            """,
            "enhancements": """
            - **OAEP-Padding:** Fügt vor der RSA-Verschlüsselung Zufälligkeit hinzu
            - **Schlüsselgrößen:** Echte Systeme verwenden 2048-4096-Bit-Schlüssel (nicht 16-Bit!)
            - **Digitale Signaturen:** Nachrichten mit dem privaten Schlüssel signieren, um Authentizität zu belegen
            - **Schlüsselablauf:** Schlüssel laufen ab und müssen erneuert werden
            """
        }

    return {
        "basics": """
        **RSA (Rivest-Shamir-Adleman)** is an asymmetric encryption algorithm that uses two keys:

        - **Public Key (e, n)**: Can be shared with anyone. Used to encrypt messages.
        - **Private Key (d, n)**: Kept secret. Used to decrypt messages.

        The magic: Something encrypted with the public key can ONLY be decrypted with the private key.
        """,
        "mathematics": """
        1. **Generate two large prime numbers** (p and q)
        2. **Calculate n** = p × q (the modulus, shared in both keys)
        3. **Calculate φ(n)** = (p-1) × (q-1) (Euler's totient)
        4. **Choose e** (public exponent) = usually 65537 (must be coprime with φ)
        5. **Calculate d** (private exponent) = the modular inverse of e (mod φ)

        **Encryption:** ciphertext = message^e mod n

        **Decryption:** message = ciphertext^d mod n
        """,
        "deterministic_issue": """
        **The Problem:** In this basic implementation, the same character always encrypts to the same number.

        Example: "hello" always becomes [542, 189, 203, 203, 445]

        An attacker can use frequency analysis to guess what letters you're encrypting!
        """,
        "hybrid_solution": """
        **Real encryption software (like GPG, PGP, Signal) use Hybrid Encryption:**

        1. **Generate a random symmetric key** (256-bit AES key)
        2. **Encrypt your actual message** with the AES key (fast, and each encryption is different!)
        3. **Encrypt the AES key** with RSA (only the 256-bit key, not the whole message)
        4. **Send both:** encrypted message + encrypted key

        **Advantages:**
        - ✅ Each encryption is different (even for the same message)
        - ✅ RSA only encrypts a small key (fast)
        - ✅ AES encryption is very fast
        - ✅ Secure against frequency analysis

        **Why not just use RSA?**
        - RSA is slow (especially with large keys)
        - RSA can only encrypt small amounts of data
        - Raw RSA is vulnerable to attacks

        This is why PGP/GPG/Signal all use this hybrid approach!
        """,
        "enhancements": """
        - **OAEP Padding:** Adds randomness before RSA encryption
        - **Key Sizes:** Real systems use 2048-4096 bit keys (not 16-bit!)
        - **Digital Signatures:** Sign messages with private key to prove authenticity
        - **Key Expiration:** Keys expire and need renewal
        """
    }
