import streamlit as st

import random

st.set_page_config(

    page_title="لغز الحروف",

    page_icon="🔐",

    layout="centered"

)

# -----------------------------

# CSS - تنسيق الصفحة

# -----------------------------

st.markdown("""
<style>

.stApp {

    text-align: center;

}

.main-title {

    font-size: 42px;

    font-weight: bold;

    margin-top: 20px;

    margin-bottom: 5px;

}

.subtitle {

    font-size: 20px;

    margin-bottom: 30px;

}

.game-box {

    padding: 25px;

    border-radius: 20px;

    border: 2px solid #e5e7eb;

    margin: 20px 0;

}

.answer-box {

    font-size: 32px;

    font-weight: bold;

    letter-spacing: 12px;

    padding: 20px;

    border-radius: 15px;

    margin: 20px 0;

}

.small-text {

    font-size: 17px;

}

div.stButton > button {

    border-radius: 12px;

    font-size: 20px;

    font-weight: bold;

    height: 55px;

}
</style>

""", unsafe_allow_html=True)


# -----------------------------

# إعداد اللعبة

# -----------------------------

ANSWER = "DATATYPES"

if "letters" not in st.session_state:

    letters = list(ANSWER)

    random.shuffle(letters)

    st.session_state.letters = letters

if "selected" not in st.session_state:

    st.session_state.selected = []

if "attempts" not in st.session_state:

    st.session_state.attempts = 0

if "message" not in st.session_state:

    st.session_state.message = ""


# -----------------------------

# العنوان

# -----------------------------

st.markdown(

    '<div class="main-title">🔐 لغز الحروف</div>',

    unsafe_allow_html=True

)

st.markdown(

    '<div class="subtitle">رتّبي الحروف واكتشفي عنوان درسنا اليوم ✨</div>',

    unsafe_allow_html=True

)

st.divider()


# -----------------------------

# الحروف

# -----------------------------

st.markdown("### 🔤 اختاري الحروف بالترتيب")

cols = st.columns(9)

for i, letter in enumerate(st.session_state.letters):

    disabled = i in st.session_state.selected

    if cols[i].button(

        letter,

        key=f"letter_{i}",

        disabled=disabled,

        use_container_width=True

    ):

        st.session_state.selected.append(i)

        st.session_state.message = ""

        st.rerun()


# -----------------------------

# الإجابة

# -----------------------------

st.markdown("### 💭 إجابتك")

selected_word = "".join(

    st.session_state.letters[i]

    for i in st.session_state.selected

)

if selected_word:

    st.markdown(

        f"""
<div class="answer-box">

            {selected_word}
</div>

        """,

        unsafe_allow_html=True

    )

else:

    st.markdown(

        """
<div class="answer-box">

            _ _ _ _ _ _ _ _ _
</div>

        """,

        unsafe_allow_html=True

    )


# -----------------------------

# الأزرار

# -----------------------------

col1, col2 = st.columns(2)

with col1:

    if st.button("✅ تحقق من الإجابة", use_container_width=True):

        st.session_state.attempts += 1

        if selected_word == ANSWER:

            st.session_state.message = "correct"

        else:

            st.session_state.message = "wrong"

        st.rerun()


with col2:

    if st.button("↩️ حذف آخر حرف", use_container_width=True):

        if st.session_state.selected:

            st.session_state.selected.pop()

        st.session_state.message = ""

        st.rerun()


# -----------------------------

# النتيجة

# -----------------------------

if st.session_state.message == "correct":

    st.success("🎉 أحسنتِ! الإجابة صحيحة")

    st.balloons()

    st.markdown(

        """
<div class="game-box">
<h1>DATA TYPES 🎯</h1>
<h2>أنواع البيانات في Python</h2>
<p class="small-text">

            🔎 لقد اكتشفتِ عنوان درسنا اليوم!
</p>
</div>

        """,

        unsafe_allow_html=True

    )


elif st.session_state.message == "wrong":

    st.error("❌ الإجابة غير صحيحة، حاولي مرة أخرى!")


# -----------------------------

# إعادة المحاولة

# -----------------------------

if st.button("🔄 إعادة اللعبة", use_container_width=True):

    letters = list(ANSWER)

    random.shuffle(letters)

    st.session_state.letters = letters

    st.session_state.selected = []

    st.session_state.message = ""

    st.rerun()


st.markdown(

    f"**المحاولات:** {st.session_state.attempts}",

)
 
