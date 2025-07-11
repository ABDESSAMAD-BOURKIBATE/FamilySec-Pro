import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os

# بيانات تدريب بسيطة (فقط كمثال)
messages = [
    "اشترِ الآن واحصل على خصم!",       # احتيال
    "تم تحديث كلمة مرورك بنجاح.",       # آمنة
    "انقر هنا للحصول على جائزة!",      # احتيال
    "مرحبًا، كيف يمكنني مساعدتك؟",     # آمنة
]

labels = ["phishing", "safe", "phishing", "safe"]

# تحويل النصوص إلى ميزات
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(messages)

# تدريب النموذج
model = LogisticRegression()
model.fit(X, labels)

# التأكد من وجود مجلد data
os.makedirs("data", exist_ok=True)

# حفظ النموذج والمتجه في ملف واحد
with open("data/model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("✅ تم تدريب النموذج وحفظه في data/model.pkl")
