import streamlit as st
from sympy import randprime
import math
import time

st.set_page_config(page_title="RSA Encryption Tool", layout="centered", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .main { max-width: 800px; }
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])
with col1:
    st.title("🔐 RSA Encryption Project")
with col2:
    st.link_button("🔗 GitHub", "https://github.com/rodi0404/RSA-Encryption-Project", use_container_width=True)

st.caption("by Rodrigo Tomann")
st.markdown("---")


# Functions from main.py
def calculatepq(bit_size):
    p = randprime(2**(bit_size-1), 2**bit_size)
    q = randprime(2**(bit_size-1), 2**bit_size)
    n = p * q
    phi = (p - 1) * (q - 1)
    return n, phi, p, q

def chooseE(phi):
    e = 65537
    if math.gcd(e, phi) != 1:
        raise ValueError("e must be coprime to phi")
    return e

def calculateD(e, phi):
    d = pow(e, -1, phi)
    return d

def encrypt(message, e, n):
    message = list(message)
    enccharlist = []
    for char in message:
        charnr = ord(char)
        encrypted = pow(charnr, e, n)
        enccharlist.append(encrypted)
    return enccharlist

def decrypt(numberlist, d, n):
    decryptedchrlist = []
    for number in numberlist:
        decryptednr = pow(number, d, n)
        decrypted = chr(decryptednr)
        decryptedchrlist.append(decrypted)
    endstring = "".join(decryptedchrlist)
    return endstring

if "keys_generated" not in st.session_state:
    st.session_state.keys_generated = False
    st.session_state.n = None
    st.session_state.e = None
    st.session_state.d = None
    st.session_state.phi = None
    st.session_state.bit_size = 16
    st.session_state.p = None
    st.session_state.q = None
    st.session_state.show_steps = False
    st.session_state.last_encrypted_message = None
    st.session_state.last_encrypted_result = None
    st.session_state.encryption_key_n = None

tab1, tab2, tab3, tab4 = st.tabs(["🔑 Generate Keys", "🔒 Encrypt", "🔓 Decrypt", "📖Infos"])

with tab1:
    st.header("Generate RSA Keys")
    st.write("Select key size and generate your public and private keys")

    def reset_steps():
        st.session_state.show_steps = False

    st.session_state.bit_size = st.radio(
        "Choose prime bit size:",
        options=[8, 16, 128],
        format_func=lambda x: f"{x}-Bit Primes" if x != 128 else "128-Bit Primes",
        horizontal=True,
        on_change=reset_steps
    )

    if st.button("Generate Keys", key="gen_keys", use_container_width=True):
        with st.spinner("Generating keys..."):
            st.session_state.n, st.session_state.phi, st.session_state.p, st.session_state.q = calculatepq(st.session_state.bit_size)
            st.session_state.e = chooseE(st.session_state.phi)
            st.session_state.d = calculateD(st.session_state.e, st.session_state.phi)
            st.session_state.keys_generated = True
            st.session_state.show_steps = True
            # Reset cached encryption when new keys are generated
            st.session_state.last_encrypted_message = None
            st.session_state.last_encrypted_result = None
            st.session_state.encryption_key_n = None

    if st.session_state.keys_generated:
        # Step definitions (reused for animation and review)
        steps = [
            {
                "title": "**Step 1:** Generate prime p",
                "content": f"""
                **Formula:** p = random prime between 2^({st.session_state.bit_size}-1) and 2^{st.session_state.bit_size}

                **Range:** {2**(st.session_state.bit_size-1):,} to {2**st.session_state.bit_size:,}

                **Result:** p = **{st.session_state.p:,}**
                """
            },
            {
                "title": "**Step 2:** Generate prime q",
                "content": f"""
                **Formula:** q = random prime between 2^({st.session_state.bit_size}-1) and 2^{st.session_state.bit_size}

                **Range:** {2**(st.session_state.bit_size-1):,} to {2**st.session_state.bit_size:,}

                **Result:** q = **{st.session_state.q:,}**
                """
            },
            {
                "title": "**Step 3:** Calculate n (modulus)",
                "content": f"""
                **Formula:** n = p × q

                **Calculation:** n = {st.session_state.p:,} × {st.session_state.q:,}

                **Result:** n = **{st.session_state.n:,}**
                """
            },
            {
                "title": "**Step 4:** Calculate φ(n) - Euler's Totient",
                "content": f"""
                **Formula:** φ(n) = (p - 1) × (q - 1)

                **Calculation:** φ(n) = ({st.session_state.p:,} - 1) × ({st.session_state.q:,} - 1)

                **Calculation:** φ(n) = {st.session_state.p - 1:,} × {st.session_state.q - 1:,}

                **Result:** φ(n) = **{st.session_state.phi:,}**
                """
            },
            {
                "title": "**Step 5:** Choose public exponent e",
                "content": f"""
                **Formula:** e = 65537 (standard choice)

                **What is GCD?**
                GCD (Greatest Common Divisor) is the largest number that divides both numbers evenly with no remainder.

                Example: gcd(12, 8) = 4 (since 4 divides both 12 and 8)

                **Why must gcd(e, φ(n)) = 1?**
                For RSA to work, e and φ(n) must be coprime (only share 1 as a common divisor). If they share other factors, we **can't** calculate the **private key d**.

                **Why use 65537?**
                - It's prime (only divisible by 1 and itself)
                - It's small (speeds up encryption)
                - It's almost always coprime with φ(n) (very rare exceptions)
                - It's the standard in cryptography (used by OpenSSL, TLS, etc.)
                - It's 10000000000000001 in binary

                **Verification:** gcd({st.session_state.e:,}, {st.session_state.phi:,}) = {math.gcd(st.session_state.e, st.session_state.phi)}

                **Result:** e = **{st.session_state.e:,}** ✅
                """
            },
            {
                "title": "**Step 6:** Calculate private exponent d",
                "content": f"""
                **Formula:** d = e^(-1) mod φ(n) (modular multiplicative inverse)

                **Meaning:** Find d such that (e × d) mod φ(n) = 1

                **Calculation:** ({st.session_state.e:,} × d) mod {st.session_state.phi:,} = 1

                **Result:** d = **{st.session_state.d:,}**

                **Verification:** ({st.session_state.e:,} × {st.session_state.d:,}) mod {st.session_state.phi:,} = {(st.session_state.e * st.session_state.d) % st.session_state.phi}
                """
            }
        ]

        # Animation only runs if show_steps is True
        if st.session_state.show_steps:
            animation_placeholder = st.empty()

            # Animate each step
            for i, step in enumerate(steps):
                with animation_placeholder.container():
                    st.markdown(f"### 🔐 {step['title']}")
                    st.markdown(step['content'])
                    st.progress((i + 1) / len(steps))
                time.sleep(2)

            animation_placeholder.empty()
            st.session_state.show_steps = False

        # Keys display - always shown when keys are generated
        st.markdown("---")
        st.success("✅ Keys Generated Successfully!")

        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Public Key (e, n)**\n\ne = {st.session_state.e}\n\nn = {st.session_state.n}")
        with col2:
            st.warning(f"**Private Key (d, n)**\n\nd = {st.session_state.d}\n\nn = {st.session_state.n}")

        st.caption(f"Verification: ({st.session_state.e} × {st.session_state.d}) mod {st.session_state.phi} = {(st.session_state.e * st.session_state.d) % st.session_state.phi}")

        st.markdown("---")
        st.subheader("📐 Complete Process (scroll down to see)")

        # Show all steps in expandable form for review
        for i, step in enumerate(steps, 1):
            with st.expander(step['title']):
                st.markdown(step['content'])

with tab2:
    st.header("Encrypt Message")

    if not st.session_state.keys_generated:
        st.warning("⚠️ Generate keys first in the 'Generate Keys' tab")
    else:
        message = st.text_input("Enter message to encrypt:", placeholder="Type your message here", key="encrypt_input")

        if message:
            # Only recalculate if message changed OR keys changed
            if (message != st.session_state.last_encrypted_message or
                st.session_state.encryption_key_n != st.session_state.n):
                encrypted = encrypt(message, st.session_state.e, st.session_state.n)
                st.session_state.last_encrypted_message = message
                st.session_state.last_encrypted_result = encrypted
                st.session_state.encryption_key_n = st.session_state.n
            else:
                encrypted = st.session_state.last_encrypted_result

            st.success("✅ Encrypted!")
            st.code(str(encrypted), language="python")

with tab3:
    st.header("Decrypt Message")

    if not st.session_state.keys_generated:
        st.warning("⚠️ Generate keys first in the 'Generate Keys' tab")
    else:
        encrypted_input = st.text_area("Enter encrypted numbers (as a list):", placeholder="[123, 456, 789, ...]")

        if encrypted_input:
            try:
                # Parse the input
                encrypted_list = eval(encrypted_input)
                if isinstance(encrypted_list, list):
                    decrypted = decrypt(encrypted_list, st.session_state.d, st.session_state.n)
                    st.success("✅ Decrypted!")
                    st.write(f"**Encrypted:**")
                    st.code(encrypted_list, language="python")
                    st.write(f"**Decrypted:**")
                    st.code(decrypted, language="text")
                else:
                    st.error("❌ Input must be a list of numbers")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("Make sure to paste the encrypted numbers in the format: [123, 456, 789, ...]")


with tab4:
    st.header("How RSA Works")

    st.subheader("🔑 The Basics")
    st.info(
        """
        **RSA (Rivest-Shamir-Adleman)** is an asymmetric encryption algorithm that uses two keys:

        - **Public Key (e, n)**: Can be shared with anyone. Used to encrypt messages.
        - **Private Key (d, n)**: Kept secret. Used to decrypt messages.

        The magic: Something encrypted with the public key can ONLY be decrypted with the private key.
        """
    )

    st.subheader("📐 How It Works Mathematically")
    st.markdown(
        """
        1. **Generate two large prime numbers** (p and q)
        2. **Calculate n** = p × q (the modulus, shared in both keys)
        3. **Calculate φ(n)** = (p-1) × (q-1) (Euler's totient)
        4. **Choose e** (public exponent) = usually 65537 (must be coprime with φ)
        5. **Calculate d** (private exponent) = the modular inverse of e (mod φ)

        **Encryption:** ciphertext = message^e mod n

        **Decryption:** message = ciphertext^d mod n
        """
    )

    st.subheader("⚠️ Security Issue: Deterministic Encryption")
    st.warning(
        """
        **The Problem:** In this basic implementation, the same character always encrypts to the same number.

        Example: "hello" always becomes [542, 189, 203, 203, 445]

        An attacker can use frequency analysis to guess what letters you're encrypting!
        """
    )

    st.subheader("🔐 How Real Systems Fix This: Hybrid Encryption")
    st.success(
        """
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
        """
    )

    st.subheader("🛡️ Real-World Security Enhancements")
    st.markdown(
        """
        - **OAEP Padding:** Adds randomness before RSA encryption
        - **Key Sizes:** Real systems use 2048-4096 bit keys (not 16-bit!)
        - **Digital Signatures:** Sign messages with private key to prove authenticity
        - **Key Expiration:** Keys expire and need renewal
        """
    )