import streamlit as st
from sympy import randprime
import math
import time
import textwrap
from content import get_tutorial_steps, get_info_content

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
    st.link_button("🔗 Github", "https://github.com/rodi0404/RSA-Encryption-Project", use_container_width=True)

st.caption("by Rodrigo Tomann")
st.markdown("---")


# Functions from main.py
def calculatepq(bit_size):
    p = randprime(2**(bit_size-1), 2**bit_size)
    q = randprime(2**(bit_size-1), 2**bit_size)
    n = p * q
    phi = (p - 1) * (q - 1)
    return n, phi, p, q

def chooseE(phi, bit_size=16):
    # For small keys, use smaller e values
    if bit_size == 8:
        candidate_e_values = [5, 17, 257]
    elif bit_size == 16:
        candidate_e_values = [17, 257, 65537]
    else:  # 128-bit and above
        candidate_e_values = [65537, 257, 17, 5, 3]

    for e in candidate_e_values:
        if e < phi and math.gcd(e, phi) == 1:
            return e

    raise ValueError(f"Could not find a suitable e for phi={phi}. Try regenerating keys.")

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

def validate_public_key(e, n):
    """Validate if e and n can work together for RSA encryption"""
    errors = []
    warnings = []

    # Check if values are positive integers
    if not isinstance(e, int) or e <= 0:
        errors.append("e must be a positive integer")
    if not isinstance(n, int) or n <= 0:
        errors.append("n must be a positive integer")

    if errors:
        return errors, warnings

    # Check if e < n (required for RSA math)
    if e >= n:
        errors.append(f"e ({e:,}) must be less than n ({n:,})")

    # Check if e and n are coprime (gcd(e, n) = 1)
    if math.gcd(e, n) != 1:
        errors.append(f"e and n must be coprime (gcd(e, n) = 1). Currently gcd({e:,}, {n:,}) = {math.gcd(e, n)}")

    # Warning if n is too small for ASCII
    if n < 256:
        warnings.append(f"⚠️ n = {n:,} is very small. ASCII characters go up to 255, so encryption may fail or produce invalid characters.")

    return errors, warnings

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
    st.session_state.tutorial_step = 0
    st.session_state.animation_step = 0
    st.session_state.animation_start_time = None
    st.session_state.animation_paused = False
    st.session_state.animation_pause_time = 0
    st.session_state.encryption_animation_step = 0
    st.session_state.encryption_animation_start_time = None
    st.session_state.encryption_animation_paused = False
    st.session_state.encryption_animation_pause_time = 0
    st.session_state.decryption_animation_step = 0
    st.session_state.decryption_animation_start_time = None
    st.session_state.decryption_animation_paused = False
    st.session_state.decryption_animation_pause_time = 0
    st.session_state.active_tab = 0

tabs = st.tabs(["📚 Tutorial", "🔑 Generate Keys", "🔒 Encrypt", "🔓 Decrypt", "📖Infos"])
tab0, tab1, tab2, tab3, tab4 = tabs

# If active_tab is set to 1, use JavaScript to click the Generate Keys tab
if st.session_state.active_tab == 1:
    st.session_state.active_tab = 0  # Reset immediately so it can be triggered again
    # Click the Generate Keys tab using Streamlit's internal mechanism
    import streamlit.components.v1 as components
    components.html("""
    <script>
    var tabs = window.parent.document.querySelectorAll('[role="tab"]');
    if (tabs.length > 1) {
        tabs[1].click();
    }
    </script>
    """, height=0)

with tab0:
    st.header("📚 How to Use This App")

    # Load tutorial steps from content module
    tutorial_steps = get_tutorial_steps()

    # Navigation
    col_left, col_center, col_right = st.columns([1, 3, 1])

    with col_left:
        if st.button("← Back", use_container_width=True, disabled=st.session_state.tutorial_step == 0):
            st.session_state.tutorial_step = max(0, st.session_state.tutorial_step - 1)
            st.rerun()

    with col_right:
        is_last_page = st.session_state.tutorial_step == len(tutorial_steps) - 1
        if st.button("Next →", use_container_width=True, disabled=False):
            if is_last_page:
                # Go to Generate Keys tab
                st.session_state.active_tab = 1
            else:
                st.session_state.tutorial_step = min(len(tutorial_steps) - 1, st.session_state.tutorial_step + 1)
            st.rerun()

    with col_center:
        step_num = st.session_state.tutorial_step + 1
        st.markdown(f"<p style='text-align: center;'>Page {step_num} of {len(tutorial_steps)}</p>", unsafe_allow_html=True)

    # Display current step
    st.markdown("---")
    current_step = tutorial_steps[st.session_state.tutorial_step]

    st.markdown(f"## {current_step['emoji']} {current_step['title']}")
    st.markdown(current_step['content'])

    # Progress indicator
    progress = st.session_state.tutorial_step / (len(tutorial_steps) - 1)
    st.progress(progress)

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
            st.session_state.e = chooseE(st.session_state.phi, st.session_state.bit_size)
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
                "duration": 8,
                "content": f"""
                **Formula:** p = random prime between 2^({st.session_state.bit_size}-1) and 2^{st.session_state.bit_size}

                **Range:** {2**(st.session_state.bit_size-1):,} to {2**st.session_state.bit_size:,}

                **Result:** p = **{st.session_state.p:,}**
                """
            },
            {
                "title": "**Step 2:** Generate prime q",
                "duration": 8,
                "content": f"""
                **Formula:** q = random prime between 2^({st.session_state.bit_size}-1) and 2^{st.session_state.bit_size}

                **Range:** {2**(st.session_state.bit_size-1):,} to {2**st.session_state.bit_size:,}

                **Result:** q = **{st.session_state.q:,}**
                """
            },
            {
                "title": "**Step 3:** Calculate n (modulus)",
                "duration": 10,
                "content": f"""
                **Formula:** n = p × q

                **Calculation:** n = {st.session_state.p:,} × {st.session_state.q:,}

                **Result:** n = **{st.session_state.n:,}**
                """
            },
            {
                "title": "**Step 4:** Calculate φ(n) - Euler's Totient",
                "duration": 12,
                "content": f"""
                **Formula:** φ(n) = (p - 1) × (q - 1)

                **Calculation:** φ(n) = ({st.session_state.p:,} - 1) × ({st.session_state.q:,} - 1)

                **Calculation:** φ(n) = {st.session_state.p - 1:,} × {st.session_state.q - 1:,}

                **Result:** φ(n) = **{st.session_state.phi:,}**
                """
            },
            {
                "title": "**Step 5:** Choose public exponent e",
                "duration": 20,
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
                "duration": 15,
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
            # Check if we've finished all steps
            if st.session_state.animation_step >= len(steps):
                st.session_state.show_steps = False
                st.session_state.animation_step = 0
                st.rerun()
            else:
                # Show current step
                current_step = steps[st.session_state.animation_step]
                step_duration = current_step.get("duration", 5)  # Get duration from step, default to 5

                st.markdown(f"### 🔐 {current_step['title']}")
                st.markdown(current_step['content'])
                st.progress((st.session_state.animation_step + 1) / len(steps))

                # Skip, Pause/Resume buttons
                col_skip, col_pause, col_timer = st.columns([1, 1, 3])

                with col_skip:
                    if st.button("⏭️ Skip", key=f"skip_button_{st.session_state.animation_step}", use_container_width=True):
                        st.session_state.animation_step += 1
                        st.session_state.animation_start_time = None
                        st.session_state.animation_paused = False
                        st.rerun()

                with col_pause:
                    pause_button_text = "▶️ Resume" if st.session_state.animation_paused else "⏸️ Pause"
                    if st.button(pause_button_text, key=f"pause_button_{st.session_state.animation_step}", use_container_width=True):
                        st.session_state.animation_paused = not st.session_state.animation_paused
                        if st.session_state.animation_paused:
                            st.session_state.animation_pause_time = time.time()
                        else:
                            # Adjust start time to account for pause duration
                            pause_duration = time.time() - st.session_state.animation_pause_time
                            st.session_state.animation_start_time += pause_duration
                        st.rerun()

                # Timer
                if st.session_state.animation_start_time is None:
                    st.session_state.animation_start_time = time.time()

                elapsed = time.time() - st.session_state.animation_start_time
                remaining = max(0, step_duration - int(elapsed))

                with col_timer:
                    if remaining > 0:
                        progress_pct = remaining / step_duration
                        timer_text = "⏸️ PAUSED" if st.session_state.animation_paused else f"⏱️ Next step in {remaining}s"
                        st.progress(progress_pct, text=timer_text)

                        if not st.session_state.animation_paused:
                            time.sleep(0.1)
                            st.rerun()
                    else:
                        st.session_state.animation_step += 1
                        st.session_state.animation_start_time = None
                        st.session_state.animation_paused = False
                        st.rerun()
        else:
            # Only show keys display after animation is complete
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

        # Option to use custom keys
        st.markdown("**Public Key Settings:**")
        use_custom_keys = st.checkbox("Use custom public key (e, n)", value=False)

        if use_custom_keys:
            col_e, col_n = st.columns(2)
            with col_e:
                custom_e = st.number_input("Enter e:", value=st.session_state.e, step=1, key="custom_e")
            with col_n:
                custom_n = st.number_input("Enter n:", value=st.session_state.n, step=1, key="custom_n")

            # Validate custom keys
            errors, warnings = validate_public_key(int(custom_e), int(custom_n))

            if errors:
                for error in errors:
                    st.error(f"❌ {error}")
                encrypt_e = None
                encrypt_n = None
            else:
                encrypt_e = int(custom_e)
                encrypt_n = int(custom_n)
                st.success(f"✅ Valid keys: e = {encrypt_e:,}, n = {encrypt_n:,}")
                if warnings:
                    for warning in warnings:
                        st.warning(warning)
        else:
            encrypt_e = st.session_state.e
            encrypt_n = st.session_state.n
            st.caption(f"Using generated keys: e = {encrypt_e:,}, n = {encrypt_n:,}")

        if message and encrypt_e is not None and encrypt_n is not None:
            # Only recalculate if message changed OR keys changed
            if (message != st.session_state.last_encrypted_message or
                st.session_state.encryption_key_n != encrypt_n):
                try:
                    encrypted = encrypt(message, encrypt_e, encrypt_n)
                    st.session_state.last_encrypted_message = message
                    st.session_state.last_encrypted_result = encrypted
                    st.session_state.encryption_key_n = encrypt_n
                except Exception as e:
                    st.error(f"❌ Encryption failed: {str(e)}")
                    encrypted = None
            else:
                encrypted = st.session_state.last_encrypted_result

            if encrypted:
                # Create step-by-step breakdown
                chars = list(message)
                ascii_values = [ord(char) for char in chars]
                ascii_display = ", ".join([f"'{char}'={ord(char)}" for char in chars])

                encryption_steps = [
                    {
                        "title": "**Step 1:** Convert message to characters",
                        "duration": 6,
                        "content": f"""
                        **Formula:** message → [char₁, char₂, ..., charₙ]

                        **Original message:** "{message}"

                        **Characters:** {chars}
                        """
                    },
                    {
                        "title": "**Step 2:** Convert each character to ASCII value",
                        "duration": 8,
                        "content": f"""
                        **Formula:** char → ord(char)

                        **Conversions:** {ascii_display}

                        **ASCII values:** {ascii_values}

                        📚 [Learn more about ASCII codes](https://www.ascii-code.com)
                        """
                    },
                    {
                        "title": "**Step 3:** Encrypt each ASCII value",
                        "duration": 10,
                        "content": textwrap.dedent(f"""
                        **Formula:** encrypted = ASCII^e mod n

                        Where e = {encrypt_e:,}, n = {encrypt_n:,}

                        **Calculations:**
                        """).strip() + "\n\n" + "\n\n".join([f"'{chars[i]}'({ascii_values[i]}) → {ascii_values[i]}^{encrypt_e:,} mod {encrypt_n:,} = {encrypted[i]:,}" for i in range(len(chars))])
                    },
                    {
                        "title": "**Step 4:** Collect into encrypted list",
                        "duration": 6,
                        "content": f"""
                        **Result:** All encrypted values combined into one list

                        **Encrypted message:** {encrypted}

                        Each number represents one character from your original message!
                        """
                    }
                ]

                # Animation system for encryption steps
                if st.session_state.encryption_animation_step < len(encryption_steps):
                    st.markdown("---")
                    st.subheader("📐 Step-by-Step Encryption Breakdown")
                    current_enc_step = encryption_steps[st.session_state.encryption_animation_step]
                    step_duration = current_enc_step.get("duration", 6)

                    st.markdown(f"### 🔐 {current_enc_step['title']}")
                    st.markdown(current_enc_step['content'])
                    st.progress((st.session_state.encryption_animation_step + 1) / len(encryption_steps))

                    # Skip, Pause/Resume buttons
                    col_skip, col_pause, col_timer = st.columns([1, 1, 3])

                    with col_skip:
                        if st.button("⏭️ Skip", key=f"enc_skip_{st.session_state.encryption_animation_step}", use_container_width=True):
                            st.session_state.encryption_animation_step += 1
                            st.session_state.encryption_animation_start_time = None
                            st.session_state.encryption_animation_paused = False
                            st.rerun()

                    with col_pause:
                        pause_button_text = "▶️ Resume" if st.session_state.encryption_animation_paused else "⏸️ Pause"
                        if st.button(pause_button_text, key=f"enc_pause_{st.session_state.encryption_animation_step}", use_container_width=True):
                            st.session_state.encryption_animation_paused = not st.session_state.encryption_animation_paused
                            if st.session_state.encryption_animation_paused:
                                st.session_state.encryption_animation_pause_time = time.time()
                            else:
                                pause_duration = time.time() - st.session_state.encryption_animation_pause_time
                                st.session_state.encryption_animation_start_time += pause_duration
                            st.rerun()

                    # Timer
                    if st.session_state.encryption_animation_start_time is None:
                        st.session_state.encryption_animation_start_time = time.time()

                    elapsed = time.time() - st.session_state.encryption_animation_start_time
                    remaining = max(0, step_duration - int(elapsed))

                    with col_timer:
                        if remaining > 0:
                            progress_pct = remaining / step_duration
                            timer_text = "⏸️ PAUSED" if st.session_state.encryption_animation_paused else f"⏱️ Next step in {remaining}s"
                            st.progress(progress_pct, text=timer_text)

                            if not st.session_state.encryption_animation_paused:
                                time.sleep(0.1)
                                st.rerun()
                        else:
                            st.session_state.encryption_animation_step += 1
                            st.session_state.encryption_animation_start_time = None
                            st.session_state.encryption_animation_paused = False
                            st.rerun()
                else:
                    # After animation completes, show final result
                    st.markdown("---")
                    st.success("✅ Encryption Complete!")
                    st.write(f"**Original:** {message}")
                    st.code(str(encrypted), language="python")

                    st.markdown("---")
                    st.subheader("📐 Complete Process (scroll down to see)")

                    # Show all steps in expandable form for review
                    for i, step in enumerate(encryption_steps, 1):
                        with st.expander(step['title']):
                            st.markdown(step['content'])
        elif message and (encrypt_e is None or encrypt_n is None):
            st.error("⚠️ Invalid keys. Please check the error messages above.")

with tab3:
    st.header("Decrypt Message")

    if not st.session_state.keys_generated:
        st.warning("⚠️ Generate keys first in the 'Generate Keys' tab")
    else:
        encrypted_input = st.text_area("Enter encrypted numbers (as a list):", placeholder="[123, 456, 789, ...]")

        # Option to use custom keys
        st.markdown("**Private Key Settings:**")
        use_custom_private_key = st.checkbox("Use custom private key (d, n)", value=False)

        if use_custom_private_key:
            col_d, col_n = st.columns(2)
            with col_d:
                custom_d = st.number_input("Enter d:", value=st.session_state.d, step=1, key="custom_d")
            with col_n:
                custom_n = st.number_input("Enter n:", value=st.session_state.n, step=1, key="custom_n")
            decrypt_d = int(custom_d)
            decrypt_n = int(custom_n)
            st.caption(f"Using custom keys: d = {decrypt_d:,}, n = {decrypt_n:,}")
        else:
            decrypt_d = st.session_state.d
            decrypt_n = st.session_state.n
            st.caption(f"Using generated keys: d = {decrypt_d:,}, n = {decrypt_n:,}")

        if encrypted_input:
            try:
                # Parse the input
                encrypted_list = eval(encrypted_input)
                if isinstance(encrypted_list, list):
                    try:
                        decrypted = decrypt(encrypted_list, decrypt_d, decrypt_n)

                        # Create step-by-step breakdown
                        ascii_values = [pow(num, decrypt_d, decrypt_n) for num in encrypted_list]
                        chars = [chr(val) for val in ascii_values]
                        ascii_display = ", ".join([f"{encrypted_list[i]}→{ascii_values[i]}" for i in range(len(encrypted_list))])

                        decryption_steps = [
                            {
                                "title": "**Step 1:** Encrypted list received",
                                "duration": 5,
                                "content": f"""
                                **Encrypted numbers:** {encrypted_list}

                                Each number represents one encrypted character.
                                """
                            },
                            {
                                "title": "**Step 2:** Decrypt each number",
                                "duration": 10,
                                "content": textwrap.dedent(f"""
                                **Formula:** ASCII = encrypted^d mod n

                                Where d = {decrypt_d:,}, n = {decrypt_n:,}

                                **Calculations:**
                                """).strip() + "\n\n" + "\n\n".join([f"{encrypted_list[i]}^{decrypt_d:,} mod {decrypt_n:,} = {ascii_values[i]}" for i in range(len(encrypted_list))])
                            },
                            {
                                "title": "**Step 3:** Convert ASCII to characters",
                                "duration": 8,
                                "content": f"""
                                **Formula:** ASCII → chr(ASCII)

                                **Conversions:** {", ".join([f"{ascii_values[i]}→'{chars[i]}'" for i in range(len(ascii_values))])}

                                📚 [Learn more about ASCII codes](https://www.ascii-code.com)
                                """
                            },
                            {
                                "title": "**Step 4:** Combine into message",
                                "duration": 6,
                                "content": f"""
                                **Result:** All characters combined into final message

                                **Decrypted message:** "{decrypted}"
                                """
                            }
                        ]

                        # Animation system for decryption steps
                        if st.session_state.decryption_animation_step < len(decryption_steps):
                            st.markdown("---")
                            st.subheader("📐 Step-by-Step Decryption Breakdown")

                            current_dec_step = decryption_steps[st.session_state.decryption_animation_step]
                            step_duration = current_dec_step.get("duration", 6)

                            st.markdown(f"### 🔐 {current_dec_step['title']}")
                            st.markdown(current_dec_step['content'])
                            st.progress((st.session_state.decryption_animation_step + 1) / len(decryption_steps))

                            # Skip, Pause/Resume buttons
                            col_skip, col_pause, col_timer = st.columns([1, 1, 3])

                            with col_skip:
                                if st.button("⏭️ Skip", key=f"dec_skip_{st.session_state.decryption_animation_step}", use_container_width=True):
                                    st.session_state.decryption_animation_step += 1
                                    st.session_state.decryption_animation_start_time = None
                                    st.session_state.decryption_animation_paused = False
                                    st.rerun()

                            with col_pause:
                                pause_button_text = "▶️ Resume" if st.session_state.decryption_animation_paused else "⏸️ Pause"
                                if st.button(pause_button_text, key=f"dec_pause_{st.session_state.decryption_animation_step}", use_container_width=True):
                                    st.session_state.decryption_animation_paused = not st.session_state.decryption_animation_paused
                                    if st.session_state.decryption_animation_paused:
                                        st.session_state.decryption_animation_pause_time = time.time()
                                    else:
                                        pause_duration = time.time() - st.session_state.decryption_animation_pause_time
                                        st.session_state.decryption_animation_start_time += pause_duration
                                    st.rerun()

                            # Timer
                            if st.session_state.decryption_animation_start_time is None:
                                st.session_state.decryption_animation_start_time = time.time()

                            elapsed = time.time() - st.session_state.decryption_animation_start_time
                            remaining = max(0, step_duration - int(elapsed))

                            with col_timer:
                                if remaining > 0:
                                    progress_pct = remaining / step_duration
                                    timer_text = "⏸️ PAUSED" if st.session_state.decryption_animation_paused else f"⏱️ Next step in {remaining}s"
                                    st.progress(progress_pct, text=timer_text)

                                    if not st.session_state.decryption_animation_paused:
                                        time.sleep(0.1)
                                        st.rerun()
                                else:
                                    st.session_state.decryption_animation_step += 1
                                    st.session_state.decryption_animation_start_time = None
                                    st.session_state.decryption_animation_paused = False
                                    st.rerun()
                        else:
                            # After animation completes, show final result
                            st.markdown("---")
                            st.success("✅ Decryption Complete!")
                            st.write(f"**Original:** {encrypted_list}")
                            st.code(decrypted, language="text")

                            st.markdown("---")
                            st.subheader("📐 Complete Process (scroll down to see)")

                            # Show all steps in expandable form for review
                            for i, step in enumerate(decryption_steps, 1):
                                with st.expander(step['title']):
                                    st.markdown(step['content'])

                    except Exception as e:
                        st.error(f"❌ Decryption failed: {str(e)}")
                        st.info("💡 Make sure you're using the correct private key (d, n) that matches the encryption key (e, n)")
                else:
                    st.error("❌ Input must be a list of numbers")
            except Exception as e:
                st.error(f"❌ Error parsing input: {str(e)}")
                st.info("Make sure to paste the encrypted numbers in the format: [123, 456, 789, ...]")


with tab4:
    st.header("How RSA Works")

    info_content = get_info_content()

    st.subheader("🔑 The Basics")
    st.info(info_content["basics"])

    st.subheader("📐 How It Works Mathematically")
    st.markdown(info_content["mathematics"])

    st.subheader("⚠️ Security Issue: Deterministic Encryption")
    st.warning(info_content["deterministic_issue"])

    st.subheader("🔐 How Real Systems Fix This: Hybrid Encryption")
    st.success(info_content["hybrid_solution"])

    st.subheader("🛡️ Real-World Security Enhancements")
    st.markdown(info_content["enhancements"])