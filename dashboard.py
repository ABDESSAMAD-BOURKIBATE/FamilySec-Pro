import streamlit as st
import pandas as pd
import pickle
import os

# =========================
# المسارات
# =========================
MODEL_PATH = "data/model.pkl"
ALERTS_FILE = "alerts.json"

# =========================
# تحميل النموذج و الـ Vectorizer
# =========================
@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)  # يُرجع (model, vectorizer)

model, vectorizer = load_model()

# =========================
# تحليل الرسالة
# =========================
def analyze_message(model, vectorizer, message):
    X = vectorizer.transform([message])
    return model.predict(X)[0]

# =========================
# تحميل / حفظ التنبيهات
# =========================
def load_alerts():
    if os.path.exists(ALERTS_FILE):
        return pd.read_json(ALERTS_FILE)
    return pd.DataFrame(columns=["message", "level"])

def save_alerts(df):
    df.to_json(ALERTS_FILE, orient="records")

alerts = load_alerts()

# =========================
# تلوين المستويات
# =========================
def level_color(row):
    if "level" not in row:
        return [""] * len(row)

    level = row["level"]
    color = ""

    if level == "phishing":
        color = "background-color: #ff4d4d; color: white"
    elif level == "http":
        color = "background-color: #ffc107; color: black"
    elif level == "safe":
        color = "background-color: #4caf50; color: white"
    else:
        color = "background-color: #e0e0e0; color: black"

    return [color if col == "level" else "" for col in row.index]

# =========================
# واجهة المستخدم
# =========================
st.set_page_config(page_title="FamilySec-Pro", layout="centered")

st.title("🔒 FamilySec-Pro - لوحة الحماية الأسرية")
st.markdown("تحليل رسائل أفراد العائلة وكشف الرسائل المشبوهة أو الاحتيالية.")

# ========== تحليل رسالة ==========
st.header("📨 تحليل رسالة جديدة")
new_msg = st.text_area("أدخل رسالة للتحليل", height=100)

if st.button("🔍 تحليل"):
    if new_msg.strip():
        level = analyze_message(model, vectorizer, new_msg)
        st.success(f"✅ تم تحليل الرسالة. النتيجة: **{level}**")

        alerts.loc[len(alerts)] = {"message": new_msg, "level": level}
        save_alerts(alerts)
    else:
        st.error("❌ الرجاء إدخال رسالة.")

# ========== سجل التنبيهات ==========
st.divider()
st.header("📋 سجل التنبيهات")

if alerts.empty:
    st.info("🚫 لا توجد رسائل بعد.")
else:
    st.dataframe(alerts.style.apply(level_color, axis=1), use_container_width=True)

# ========== التذييل ==========
st.divider()
st.markdown(
    """
    <div style='text-align:center; font-size: 14px; color: gray;'>
    المطور: <b>عبد الصمد بوركيبات</b> | الإصدار: <b>1.0</b> | الترخيص: <b>MIT</b><br>
    &copy; 2025 عبد الصمد بوركيبات - جميع الحقوق محفوظة.
    </div>
    """,
    unsafe_allow_html=True
)
