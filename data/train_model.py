import os
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ========= 1. البيانات التدريبية البسيطة =========
data = {
    "message": [
        "مرحباً بك، هذه رسالة آمنة",             # safe
        "انقر هنا للحصول على الجائزة",            # phishing
        "يرجى تحديث كلمة مرورك فوراً",             # phishing
        "هذا رابط تسجيل الدخول: http://xyz.com",  # http
        "كل شيء على ما يرام، لا تقلق",            # safe
        "تم اختراق حسابك، انقر هنا",              # phishing
        "تحديث جديد للنظام متوفر الآن",            # safe
        "للحصول على خصم اضغط على الرابط"          # phishing
    ],
    "label": [
        "safe",
        "phishing",
        "phishing",
        "http",
        "safe",
        "phishing",
        "safe",
        "phishing"
    ]
}

df = pd.DataFrame(data)

# ========= 2. تجهيز الـ Vectorizer =========
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["message"])
y = df["label"]

# ========= 3. تدريب نموذج الانحدار اللوجستي =========
model = LogisticRegression()
model.fit(X, y)

# ========= 4. حفظ النموذج والـ Vectorizer =========
os.makedirs("data", exist_ok=True)
with open("data/model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("✅ تم تدريب النموذج وحفظه في data/model.pkl")
