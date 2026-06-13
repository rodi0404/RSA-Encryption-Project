"""
Content strings and data structures for the RSA Encryption Tool.
This file contains all the tutorial steps, info content, and educational text.
"""

def get_tutorial_steps():
    """Returns the tutorial steps for the "How to Use This App" section."""
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


def get_info_content():
    """Returns the content for the 'How RSA Works' info tab."""
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
