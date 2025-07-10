import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

MODEL_PATH = "app/model.pkl"

def train_and_save_model():
    df = pd.read_csv("data/train_messages.csv")
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(df['message'], df['label'])
    joblib.dump(model, MODEL_PATH)
    print(" تم تدريب النموذج وتخزينه في model.pkl")
    return model

def load_model():
    if os.path.exists(MODEL_PATH):
        print(" تحميل النموذج من model.pkl...")
        return joblib.load(MODEL_PATH)
    else:
        print(" لا يوجد نموذج مخزَّن، سيتم تدريبه الآن...")
        return train_and_save_model()

def analyze_message(model, message):
    prediction = model.predict([message])[0]
    return prediction

def analyze_file(model, filepath):
    if not os.path.exists(filepath):
        print(f" الملف {filepath} غير موجود.")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        messages = f.readlines()
    print(f"\n تحليل {len(messages)} رسالة من الملف: {filepath}\n")
    for i, message in enumerate(messages, 1):
        message = message.strip()
        if not message:
            continue
        pred = analyze_message(model, message)
        label_map = {
            "safe": "✅ آمنة",
            "phishing": "⚠️ احتيالية",
            "http": "🚨 رابط مشبوه"
        }
        print(f"{i}. {message}\n   النتيجة: {label_map.get(pred, '🔘 غير معروف')}\n")

def run_analysis():
    model = load_model()
    print("اختر نوع التحليل:\n1. رسالة واحدة\n2. ملف رسائل")
    choice = input("> ").strip()
    if choice == "1":
        test_message = input("📩 أدخل الرسالة لتحليلها:\n> ")
        prediction = analyze_message(model, test_message)
        label_map = {
            "safe": "✅ لا يوجد تهديد.",
            "phishing": "⚠️ الرسالة تبدو كعملية احتيال.",
            "http": "🚨 تحتوي على رابط مشبوه."
        }
        print("\n🔍 تم تحليل الرسالة. النتيجة:")
        print(label_map.get(prediction, "🔘 لم يتم التعرف على نوع الرسالة."))
    elif choice == "2":
        filepath = input("📂 أدخل مسار ملف الرسائل (مثال: data/bulk_messages.txt):\n> ")
        analyze_file(model, filepath)
    else:
        print("❌ اختيار غير صالح، يرجى المحاولة مجددًا.")
