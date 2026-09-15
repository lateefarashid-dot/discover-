import streamlit as st
import random
st.set_page_config(
   page_title="لغز الحروف",
   page_icon="🔐",
   layout="centered"
)
# -----------------------------
# إعدادات اللعبة
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
if "finished" not in st.session_state:
   st.session_state.finished = False

# -----------------------------
# العنوان
# -----------------------------
st.title("🔐 لغز الحروف")
st.write("رتّبي الحروف لتكتشفي عنوان درسنا لهذا اليوم 👀")
st.divider()
# -----------------------------
# عرض الحروف
# -----------------------------
st.subheader("🔤 الحروف المتاحة")
cols = st.columns(9)
for i, letter in enumerate(st.session_state.letters):
   # إذا كان الحرف مستخدمًا نخليه غير قابل للضغط
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
# الحروف المختارة
# -----------------------------
st.divider()
st.subheader("✨ إجابتك:")
selected_word = "".join(
   st.session_state.letters[i]
   for i in st.session_state.selected
)
if selected_word:
   # نعرضها بشكل أجمل
   st.markdown(
       f"<h2 style='text-align:center; letter-spacing:12px;'>"
       f"{selected_word}"
       f"</h2>",
       unsafe_allow_html=True
   )


# -----------------------------
# الأزرار
# -----------------------------
col1, col2, col3 = st.columns(3)
with col1:
   if st.button("✅ تحقق", use_container_width=True):
       st.session_state.attempts += 1
       if selected_word == ANSWER:
           st.session_state.message = "correct"
           st.session_state.finished = True
       else:
           st.session_state.message = "wrong"
       st.rerun()

with col2:
   if st.button("↩️ حذف آخر حرف", use_container_width=True):
       if st.session_state.selected:
           st.session_state.selected.pop()
       st.session_state.message = ""
       st.rerun()

with col3:
   if st.button("🔄 إعادة المحاولة", use_container_width=True):
       letters = list(ANSWER)
       random.shuffle(letters)
       st.session_state.letters = letters
       st.session_state.selected = []
       st.session_state.message = ""
       st.session_state.finished = False
       st.rerun()

# -----------------------------
# النتيجة
# -----------------------------
if st.session_state.message == "correct":
   st.success("🎉 إجابة صحيحة!")
   st.balloons()
   st.markdown(
       """
<div style="text-align:center;">
<h1>DATA TYPES 🎯</h1>
<h2>أنواع البيانات في لغة بايثون</h2>
<p>✨ اكتشفنا عنوان درسنا اليوم!</p>
</div>
       """,
       unsafe_allow_html=True
   )
elif st.session_state.message == "wrong":
   st.error("❌ إجابة خاطئة، حاولي مرة أخرى!")
# -----------------------------
# عدد المحاولات
# -----------------------------
st.caption(f"🔢 عدد المحاولات: {st.session_state.attempts}")
