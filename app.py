import streamlit as st
from sympy import randprime
import math
import time
from content import get_tutorial_steps, get_info_content, get_asymmetric_explanation_intro, get_asymmetric_explanation_outro
from i18n import LANGUAGES, UI_TEXT, KEYGEN_STEP_TEMPLATES, ENCRYPT_STEP_TEMPLATES, DECRYPT_STEP_TEMPLATES

st.set_page_config(page_title="RSA Encryption Tool", layout="centered", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .main { max-width: 800px; }
    [data-testid="stHeaderActionElements"] { display: none; }
    [data-testid="stHeading"] h1 { white-space: nowrap !important; font-size: clamp(1.1rem, 3.5vw, 2.25rem) !important; }
    </style>
""", unsafe_allow_html=True)

if "lang" not in st.session_state:
    st.session_state.lang = "en"

st.segmented_control(
    "Language",
    options=["en", "de"],
    format_func=lambda x: LANGUAGES[x],
    key="lang",
    required=True,
    label_visibility="collapsed",
)

T = UI_TEXT[st.session_state.lang]

col1, col2 = st.columns([5, 1])
with col1:
    st.title(T["app_title"])
with col2:
    st.link_button(T["github_button"], "https://github.com/rodi0404/RSA-Encryption-Project", use_container_width=True)

st.caption(T["caption"])
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

def validate_public_key(e, n, T):
    """Validate if e and n can work together for RSA encryption"""
    errors = []
    warnings = []

    # Check if values are positive integers
    if not isinstance(e, int) or e <= 0:
        errors.append(T["err_e_not_positive"])
    if not isinstance(n, int) or n <= 0:
        errors.append(T["err_n_not_positive"])

    if errors:
        return errors, warnings

    # Check if e < n (required for RSA math)
    if e >= n:
        errors.append(T["err_e_too_large"].format(e=f"{e:,}", n=f"{n:,}"))

    # Check if e and n are coprime (gcd(e, n) = 1)
    if math.gcd(e, n) != 1:
        errors.append(T["err_not_coprime"].format(e=f"{e:,}", n=f"{n:,}", gcd=math.gcd(e, n)))

    # Warning if n is too small for ASCII
    if n < 256:
        warnings.append(T["warn_n_small"].format(n=f"{n:,}"))

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
    st.session_state.show_asymmetric_explanation = False

tabs = st.tabs([T["tab_tutorial"], T["tab_generate"], T["tab_encrypt"], T["tab_decrypt"], T["tab_infos"]])
tab0, tab1, tab2, tab3, tab4 = tabs

# If active_tab is set to 1, use JavaScript to click the Generate Keys tab
if st.session_state.active_tab == 1:
    st.session_state.active_tab = 0  # Reset immediately so it can be triggered again
    # Click the Generate Keys tab using Streamlit's internal mechanism
    st.iframe("""
    <script>
    var tabs = window.parent.document.querySelectorAll('[role="tab"]');
    if (tabs.length > 1) {
        tabs[1].click();
    }
    </script>
    """, height=1)

with tab0:
    st.header(T["tutorial_header"])

    if st.session_state.show_asymmetric_explanation:
        if st.button(T["back_to_tutorial"], use_container_width=True):
            st.session_state.show_asymmetric_explanation = False
            st.rerun()

        st.markdown("---")
        st.markdown(f"## {T['asymmetric_header']}")
        st.markdown(get_asymmetric_explanation_intro(st.session_state.lang))
        st.image("image.png", caption=T["asymmetric_image_caption"])
        st.markdown(get_asymmetric_explanation_outro(st.session_state.lang))
    else:
        # Load tutorial steps from content module
        tutorial_steps = get_tutorial_steps(st.session_state.lang)

        # Navigation
        col_left, col_center, col_right = st.columns([1, 3, 1])

        with col_left:
            if st.button(T["back"], use_container_width=True, disabled=st.session_state.tutorial_step == 0):
                st.session_state.tutorial_step = max(0, st.session_state.tutorial_step - 1)
                st.rerun()

        with col_right:
            is_last_page = st.session_state.tutorial_step == len(tutorial_steps) - 1
            if st.button(T["next"], use_container_width=True, disabled=False):
                if is_last_page:
                    # Go to Generate Keys tab
                    st.session_state.active_tab = 1
                else:
                    st.session_state.tutorial_step = min(len(tutorial_steps) - 1, st.session_state.tutorial_step + 1)
                st.rerun()

        with col_center:
            step_num = st.session_state.tutorial_step + 1
            st.markdown(f"<p style='text-align: center;'>{T['page_of'].format(current=step_num, total=len(tutorial_steps))}</p>", unsafe_allow_html=True)

        # Display current step
        st.markdown("---")
        current_step = tutorial_steps[st.session_state.tutorial_step]

        st.markdown(f"## {current_step['emoji']} {current_step['title']}")
        st.markdown(current_step['content'])

        if st.session_state.tutorial_step == 1:
            if st.button(T["asymmetric_btn"], use_container_width=True):
                st.session_state.show_asymmetric_explanation = True
                st.rerun()

        # Progress indicator
        progress = st.session_state.tutorial_step / (len(tutorial_steps) - 1)
        st.progress(progress)

with tab1:
    st.header(T["gen_header"])
    st.write(T["gen_subtitle"])

    def reset_steps():
        st.session_state.show_steps = False

    st.session_state.bit_size = st.radio(
        T["gen_radio_label"],
        options=[8, 16, 128],
        format_func=lambda x: T["gen_bit_format"].format(bits=x),
        horizontal=True,
        on_change=reset_steps
    )

    if st.button(T["gen_button"], key="gen_keys", use_container_width=True):
        with st.spinner(T["gen_spinner"]):
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
        bit_size = st.session_state.bit_size
        p, q, n, phi, e, d = (
            st.session_state.p, st.session_state.q, st.session_state.n,
            st.session_state.phi, st.session_state.e, st.session_state.d,
        )
        templates = KEYGEN_STEP_TEMPLATES[st.session_state.lang]
        low = f"{2**(bit_size-1):,}"
        high = f"{2**bit_size:,}"

        # Step definitions (reused for animation and review)
        steps = [
            {
                "title": templates[0]["title"],
                "duration": 8,
                "content": templates[0]["content"].format(bits=bit_size, low=low, high=high, p=f"{p:,}"),
            },
            {
                "title": templates[1]["title"],
                "duration": 8,
                "content": templates[1]["content"].format(bits=bit_size, low=low, high=high, q=f"{q:,}"),
            },
            {
                "title": templates[2]["title"],
                "duration": 10,
                "content": templates[2]["content"].format(p=f"{p:,}", q=f"{q:,}", n=f"{n:,}"),
            },
            {
                "title": templates[3]["title"],
                "duration": 12,
                "content": templates[3]["content"].format(
                    p=f"{p:,}", q=f"{q:,}", phi=f"{phi:,}",
                    p_minus_1=f"{p - 1:,}", q_minus_1=f"{q - 1:,}",
                ),
            },
            {
                "title": templates[4]["title"],
                "duration": 20,
                "content": templates[4]["content"].format(e=f"{e:,}", phi=f"{phi:,}", gcd=math.gcd(e, phi)),
            },
            {
                "title": templates[5]["title"],
                "duration": 15,
                "content": templates[5]["content"].format(e=f"{e:,}", phi=f"{phi:,}", d=f"{d:,}", verify=(e * d) % phi),
            },
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
                    if st.button(T["skip"], key=f"skip_button_{st.session_state.animation_step}", use_container_width=True):
                        st.session_state.animation_step += 1
                        st.session_state.animation_start_time = None
                        st.session_state.animation_paused = False
                        st.rerun()

                with col_pause:
                    pause_button_text = T["resume"] if st.session_state.animation_paused else T["pause"]
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
                        timer_text = T["paused"] if st.session_state.animation_paused else T["next_step_in"].format(seconds=remaining)
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
            st.success(T["keys_success"])

            col1, col2 = st.columns(2)
            with col1:
                st.info(T["public_key_box"].format(e=e, n=n))
            with col2:
                st.warning(T["private_key_box"].format(d=d, n=n))

            st.caption(T["verification_caption"].format(e=e, d=d, phi=phi, result=(e * d) % phi))

            st.markdown("---")
            st.subheader(T["complete_process"])

            # Show all steps in expandable form for review
            for i, step in enumerate(steps, 1):
                with st.expander(step['title']):
                    st.markdown(step['content'])

with tab2:
    st.header(T["encrypt_header"])

    if not st.session_state.keys_generated:
        st.warning(T["need_keys_warning"])
    else:
        message = st.text_input(T["encrypt_input_label"], placeholder=T["encrypt_input_placeholder"], key="encrypt_input")

        # Option to use custom keys
        st.markdown(T["public_key_settings"])
        use_custom_keys = st.checkbox(T["use_custom_public_key"], value=False)

        if use_custom_keys:
            col_e, col_n = st.columns(2)
            with col_e:
                custom_e = st.number_input(T["enter_e"], value=st.session_state.e, step=1, key="custom_e")
            with col_n:
                custom_n = st.number_input(T["enter_n"], value=st.session_state.n, step=1, key="custom_n")

            # Validate custom keys
            errors, warnings = validate_public_key(int(custom_e), int(custom_n), T)

            if errors:
                for error in errors:
                    st.error(f"❌ {error}")
                encrypt_e = None
                encrypt_n = None
            else:
                encrypt_e = int(custom_e)
                encrypt_n = int(custom_n)
                st.success(T["valid_keys"].format(e=f"{encrypt_e:,}", n=f"{encrypt_n:,}"))
                if warnings:
                    for warning in warnings:
                        st.warning(warning)
        else:
            encrypt_e = st.session_state.e
            encrypt_n = st.session_state.n
            st.caption(T["using_generated_keys"].format(e=f"{encrypt_e:,}", n=f"{encrypt_n:,}"))

        if message and encrypt_e is not None and encrypt_n is not None:
            # Only recalculate if message changed OR keys changed
            if (message != st.session_state.last_encrypted_message or
                st.session_state.encryption_key_n != encrypt_n):
                try:
                    encrypted = encrypt(message, encrypt_e, encrypt_n)
                    st.session_state.last_encrypted_message = message
                    st.session_state.last_encrypted_result = encrypted
                    st.session_state.encryption_key_n = encrypt_n
                except Exception as ex:
                    st.error(T["encryption_failed"].format(error=str(ex)))
                    encrypted = None
            else:
                encrypted = st.session_state.last_encrypted_result

            if encrypted:
                # Create step-by-step breakdown
                chars = list(message)
                ascii_values = [ord(char) for char in chars]
                ascii_display = ", ".join([f"'{char}'={ord(char)}" for char in chars])
                calculations = "\n\n".join([f"'{chars[i]}'({ascii_values[i]}) → {ascii_values[i]}^{encrypt_e:,} mod {encrypt_n:,} = {encrypted[i]:,}" for i in range(len(chars))])

                enc_templates = ENCRYPT_STEP_TEMPLATES[st.session_state.lang]
                encryption_steps = [
                    {
                        "title": enc_templates[0]["title"],
                        "duration": 6,
                        "content": enc_templates[0]["content"].format(message=message, chars=chars),
                    },
                    {
                        "title": enc_templates[1]["title"],
                        "duration": 8,
                        "content": enc_templates[1]["content"].format(ascii_display=ascii_display, ascii_values=ascii_values),
                    },
                    {
                        "title": enc_templates[2]["title"],
                        "duration": 10,
                        "content": enc_templates[2]["content"].format(e=f"{encrypt_e:,}", n=f"{encrypt_n:,}", calculations=calculations),
                    },
                    {
                        "title": enc_templates[3]["title"],
                        "duration": 6,
                        "content": enc_templates[3]["content"].format(encrypted=encrypted),
                    },
                ]

                # Animation system for encryption steps
                if st.session_state.encryption_animation_step < len(encryption_steps):
                    st.markdown("---")
                    st.subheader(T["encryption_breakdown"])
                    current_enc_step = encryption_steps[st.session_state.encryption_animation_step]
                    step_duration = current_enc_step.get("duration", 6)

                    st.markdown(f"### 🔐 {current_enc_step['title']}")
                    st.markdown(current_enc_step['content'])
                    st.progress((st.session_state.encryption_animation_step + 1) / len(encryption_steps))

                    # Skip, Pause/Resume buttons
                    col_skip, col_pause, col_timer = st.columns([1, 1, 3])

                    with col_skip:
                        if st.button(T["skip"], key=f"enc_skip_{st.session_state.encryption_animation_step}", use_container_width=True):
                            st.session_state.encryption_animation_step += 1
                            st.session_state.encryption_animation_start_time = None
                            st.session_state.encryption_animation_paused = False
                            st.rerun()

                    with col_pause:
                        pause_button_text = T["resume"] if st.session_state.encryption_animation_paused else T["pause"]
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
                            timer_text = T["paused"] if st.session_state.encryption_animation_paused else T["next_step_in"].format(seconds=remaining)
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
                    st.success(T["encryption_complete"])
                    st.write(T["original_label"].format(value=message))
                    st.code(str(encrypted), language="python")

                    st.markdown("---")
                    st.subheader(T["complete_process"])

                    # Show all steps in expandable form for review
                    for i, step in enumerate(encryption_steps, 1):
                        with st.expander(step['title']):
                            st.markdown(step['content'])
        elif message and (encrypt_e is None or encrypt_n is None):
            st.error(T["invalid_keys_error"])

with tab3:
    st.header(T["decrypt_header"])

    if not st.session_state.keys_generated:
        st.warning(T["need_keys_warning"])
    else:
        encrypted_input = st.text_area(T["decrypt_input_label"], placeholder=T["decrypt_input_placeholder"])

        # Option to use custom keys
        st.markdown(T["private_key_settings"])
        use_custom_private_key = st.checkbox(T["use_custom_private_key"], value=False)

        if use_custom_private_key:
            col_d, col_n = st.columns(2)
            with col_d:
                custom_d = st.number_input(T["enter_d"], value=st.session_state.d, step=1, key="custom_d")
            with col_n:
                custom_n = st.number_input(T["enter_n"], value=st.session_state.n, step=1, key="custom_n")
            decrypt_d = int(custom_d)
            decrypt_n = int(custom_n)
            st.caption(T["using_custom_keys_dn"].format(d=f"{decrypt_d:,}", n=f"{decrypt_n:,}"))
        else:
            decrypt_d = st.session_state.d
            decrypt_n = st.session_state.n
            st.caption(T["using_generated_keys_dn"].format(d=f"{decrypt_d:,}", n=f"{decrypt_n:,}"))

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
                        calculations = "\n\n".join([f"{encrypted_list[i]}^{decrypt_d:,} mod {decrypt_n:,} = {ascii_values[i]}" for i in range(len(encrypted_list))])
                        conversions = ", ".join([f"{ascii_values[i]}→'{chars[i]}'" for i in range(len(ascii_values))])

                        dec_templates = DECRYPT_STEP_TEMPLATES[st.session_state.lang]
                        decryption_steps = [
                            {
                                "title": dec_templates[0]["title"],
                                "duration": 5,
                                "content": dec_templates[0]["content"].format(encrypted_list=encrypted_list),
                            },
                            {
                                "title": dec_templates[1]["title"],
                                "duration": 10,
                                "content": dec_templates[1]["content"].format(d=f"{decrypt_d:,}", n=f"{decrypt_n:,}", calculations=calculations),
                            },
                            {
                                "title": dec_templates[2]["title"],
                                "duration": 8,
                                "content": dec_templates[2]["content"].format(conversions=conversions),
                            },
                            {
                                "title": dec_templates[3]["title"],
                                "duration": 6,
                                "content": dec_templates[3]["content"].format(decrypted=decrypted),
                            },
                        ]

                        # Animation system for decryption steps
                        if st.session_state.decryption_animation_step < len(decryption_steps):
                            st.markdown("---")
                            st.subheader(T["decryption_breakdown"])

                            current_dec_step = decryption_steps[st.session_state.decryption_animation_step]
                            step_duration = current_dec_step.get("duration", 6)

                            st.markdown(f"### 🔐 {current_dec_step['title']}")
                            st.markdown(current_dec_step['content'])
                            st.progress((st.session_state.decryption_animation_step + 1) / len(decryption_steps))

                            # Skip, Pause/Resume buttons
                            col_skip, col_pause, col_timer = st.columns([1, 1, 3])

                            with col_skip:
                                if st.button(T["skip"], key=f"dec_skip_{st.session_state.decryption_animation_step}", use_container_width=True):
                                    st.session_state.decryption_animation_step += 1
                                    st.session_state.decryption_animation_start_time = None
                                    st.session_state.decryption_animation_paused = False
                                    st.rerun()

                            with col_pause:
                                pause_button_text = T["resume"] if st.session_state.decryption_animation_paused else T["pause"]
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
                                    timer_text = T["paused"] if st.session_state.decryption_animation_paused else T["next_step_in"].format(seconds=remaining)
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
                            st.success(T["decryption_complete"])
                            st.write(T["original_label"].format(value=encrypted_list))
                            st.code(decrypted, language="text")

                            st.markdown("---")
                            st.subheader(T["complete_process"])

                            # Show all steps in expandable form for review
                            for i, step in enumerate(decryption_steps, 1):
                                with st.expander(step['title']):
                                    st.markdown(step['content'])

                    except Exception as ex:
                        st.error(T["decryption_failed"].format(error=str(ex)))
                        st.info(T["decryption_failed_hint"])
                else:
                    st.error(T["input_must_be_list"])
            except Exception as ex:
                st.error(T["parse_error"].format(error=str(ex)))
                st.info(T["parse_error_hint"])


with tab4:
    st.header(T["info_header"])

    info_content = get_info_content(st.session_state.lang)

    st.subheader(T["info_basics_title"])
    st.info(info_content["basics"])

    st.subheader(T["info_math_title"])
    st.markdown(info_content["mathematics"])

    st.subheader(T["info_deterministic_title"])
    st.warning(info_content["deterministic_issue"])

    st.subheader(T["info_hybrid_title"])
    st.success(info_content["hybrid_solution"])

    st.subheader(T["info_enhancements_title"])
    st.markdown(info_content["enhancements"])
