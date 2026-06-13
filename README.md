# 🔐 RSA Encryption Tool

An interactive educational web application that teaches RSA encryption step-by-step with animated visualizations and hands-on demonstrations.

## Overview

This project is a **Streamlit-based learning tool** designed to help students and cryptography enthusiasts understand how RSA encryption works mathematically. Instead of just reading about RSA, users can:

- 🔑 **Generate their own RSA key pairs** and watch the mathematical process unfold step-by-step
- 🔒 **Encrypt messages** with animated breakdowns of each calculation
- 🔓 **Decrypt messages** to verify the process is reversible
- 📚 **Learn the theory** behind RSA with explanations of the mathematics
- 🧪 **Experiment with custom keys** to understand how RSA security works

## Features

### 📚 Tutorial Tab
A guided introduction covering:
- What RSA is and why it matters
- Key generation explained
- Encryption and decryption process
- Testing with custom keys
- Real-world security considerations

### 🔑 Generate Keys Tab
- Choose between 8-bit, 16-bit, or 128-bit prime numbers
- Watch a 6-step animated process:
  1. Generate prime p
  2. Generate prime q
  3. Calculate n = p × q
  4. Calculate φ(n) = (p-1) × (q-1)
  5. Choose e (public exponent)
  6. Calculate d (private exponent)
- View the generated public and private keys
- Review the complete mathematical process

### 🔒 Encrypt Tab
- Enter any message to encrypt
- Watch 4 animated steps:
  1. Convert message to characters
  2. Convert characters to ASCII values (with link to ASCII reference)
  3. Encrypt each ASCII value using the formula: `encrypted = ASCII^e mod n`
  4. Collect into final encrypted list
- Option to use custom public keys for testing
- View the complete encryption process

### 🔓 Decrypt Tab
- Paste encrypted numbers to decrypt
- Watch 4 animated steps:
  1. Receive encrypted list
  2. Decrypt each number using: `ASCII = encrypted^d mod n`
  3. Convert ASCII values back to characters (with ASCII reference link)
  4. Combine into readable message
- Option to use custom private keys
- Verify that only the matching private key can decrypt

### 📖 Info Tab
Learn about:
- RSA basics and how it works mathematically
- The deterministic encryption issue in basic RSA
- How real-world systems solve it with hybrid encryption
- Real-world security enhancements (OAEP, key sizes, digital signatures)

## Technical Stack

- **Framework**: [Streamlit](https://streamlit.io/) - Python web app framework
- **Cryptography**: [SymPy](https://www.sympy.org/) - For prime number generation and modular arithmetic
- **Language**: Python 3
- **Frontend**: Streamlit components with custom HTML/JavaScript for tab switching

## Installation & Setup

### Requirements
- Python 3.7+
- pip (Python package manager)

### Steps

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd encryption
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   - The app should open automatically at `http://localhost:8501`
   - If not, copy the URL from the terminal

## Project Structure

```
encryption/
├── app.py                 # Main Streamlit application
├── content.py            # Educational content (tutorial, info)
├── main.py              # Original RSA implementation (reference)
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## How It Works

### RSA Key Generation
1. Choose two large random prime numbers: p and q
2. Calculate n = p × q (the modulus)
3. Calculate φ(n) = (p-1) × (q-1) (Euler's totient function)
4. Choose e (public exponent), typically 65537, such that gcd(e, φ(n)) = 1
5. Calculate d (private exponent) = the modular inverse of e mod φ(n)
6. **Public key**: (e, n)
7. **Private key**: (d, n)

### RSA Encryption
```
For each character:
1. Convert character to ASCII value
2. Calculate: ciphertext = plaintext^e mod n
3. Send the encrypted numbers
```

### RSA Decryption
```
For each encrypted number:
1. Calculate: plaintext = ciphertext^d mod n
2. Convert back to ASCII character
3. Combine all characters into original message
```

## Educational Value

This tool is perfect for:
- 🎓 Computer Science students learning cryptography
- 👨‍💻 Developers wanting to understand RSA fundamentals
- 🔐 Security enthusiasts exploring encryption mathematics
- 📚 Anyone curious about how HTTPS and digital signatures work

**Note**: This implementation uses small key sizes (8-128 bit) for educational purposes. Real-world RSA uses 2048-4096 bit keys for security.

## Limitations & Security Notes

⚠️ **Educational Use Only**: This tool is designed for learning, not production use.

- Small key sizes (not cryptographically secure)
- Deterministic encryption (same plaintext always produces same ciphertext)
- No padding (basic textbook RSA)
- Limited message size (characters must be < n)

**Real-world solutions** like GPG, PGP, and TLS use:
- Hybrid encryption (RSA + AES)
- OAEP padding for randomness
- Larger key sizes (2048+ bits)
- Digital signatures for authentication

## Attribution

**Code & Algorithm Implementation**: Written by [Rodrigo Tomann](https://github.com/rodi0404)

The core code for calculating keys, encrypting, decrypting, and all cryptographic functions was written from scratch. **AI was mainly used for the text/copywriting and educational content** of the application (tutorial explanations, info sections, step descriptions).

**This project was NOT vibecoded.** While the colorful design with emojis might suggest otherwise, the cryptographic implementation and application logic are handwritten code, not AI-generated.

## Acknowledgments

- [SymPy](https://www.sympy.org/) for prime number generation and modular arithmetic
- [Streamlit](https://streamlit.io/) for the excellent Python web framework
- [ASCII Code](https://www.ascii-code.com/) reference used in the application


## Contact & Links

- 🔗 [GitHub Repository](https://github.com/rodi0404/RSA-Encryption-Project)
- 📧 Email: rodibb0404@gmail.com

---

**Happy learning! Explore cryptography interactively! 🚀**
