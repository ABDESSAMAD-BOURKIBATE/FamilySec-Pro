"""
===============================================================================
                        FamilySec System - كشف الاحتيال
===============================================================================

المطور: عبد الصمد بوركيبات
الإصدار: 1.0 - 2025
الرخصة: MIT License

حقوق النشر (c) 2025 عبد الصمد بوركيبات. جميع الحقوق محفوظة.

الوصف:
برنامج تحليل وتصنيف الرسائل لاكتشاف محاولات الاحتيال والروابط المشبوهة
باستخدام نموذج تصنيف مبني على Naive Bayes مع تمثيل TF-IDF.

===============================================================================
"""

import os
import sys
import time
from datetime import datetime
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
from colorama import init, Fore, Style

# تهيئة colorama مع إعادة تعيين تلقائية للألوان
init(autoreset=True)

MODEL_PATH = "app/model.pkl"

def fancy_print(text: str, color=Fore.CYAN, delay=0.005):
    """
    طباعة نص مع تأثير كتابة حرف بحرف (لجذب الانتباه)
    """
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)  # إعادة تعيين النمط بعد الطباعة

def show_welcome():
    border = "═" * 47
    header = f"{Fore.MAGENTA}{Style.BRIGHT}  FamilySec System  -  كشف محاولات الاحتيال  "
    author = f"{Fore.YELLOW}المطور: عبد الصمد بوركيبات"
    version = f"{Fore.GREEN}الإصدار: 1.0 - 2025"
    license_info = f"{Fore.BLUE}الرخصة: MIT License"
    
    print(Fore.MAGENTA + "╔" + border + "╗")
    print("║" + " " * 47 + "║")
    print("║" + header.center(47) + "║")
    print("║" + " " * 47 + "║")
    print("║" + author.center(47) + "║")
    print("║" + version.center(47) + "║")
    print("║" + license_info.center(47) + "║")
    print("║" + " " * 47 + "║")
    print(Fore.MAGENTA + "╚" + border + "╝\n")

def print_start_time():
    now = datetime.now()
    print(Fore.CYAN + f"⏰ وقت بدء البرنامج: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

def train_and_save_model():
    try:
        df = pd.read_csv("data/train_messages.csv")
    except FileNotFoundError:
        print(Fore.RED + "❌ ملف البيانات 'data/train_messages.csv' غير موجود. الرجاء التأكد من وجود الملف.")
        sys.exit(1)
    df = df.dropna(subset=['message', 'label'])  # تنظيف القيم الفارغة
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    print(Fore.YELLOW + "⏳ جاري تدريب النموذج، يرجى الانتظار ...")
    model.fit(df['message'], df['label'])
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(Fore.GREEN + "✅ تم تدريب النموذج وتخزينه بنجاح في model.pkl\n")
    return model

def load_model():
    if os.path.exists(MODEL_PATH):
        print(Fore.CYAN + "🔄 تحميل النموذج من ملف model.pkl ...")
        return joblib.load(MODEL_PATH)
    else:
        print(Fore.YELLOW + "⚠️ لا يوجد نموذج مخزن، سيتم تدريبه الآن ...")
        return train_and_save_model()

def analyze_message(model, message: str) -> str:
    prediction = model.predict([message])[0]
    return prediction

def analyze_file(model, filepath: str):
    if not os.path.exists(filepath):
        print(Fore.RED + f"❌ الملف '{filepath}' غير موجود.")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        messages = f.readlines()
    print(Fore.BLUE + f"\n📊 تحليل {len(messages)} رسالة من الملف: {filepath}\n")
    
    label_map = {
        "safe": Fore.GREEN + "✅ آمنة",
        "phishing": Fore.RED + "⚠ احتيالية",
        "http": Fore.MAGENTA + "🚨 رابط مشبوه"
    }

    for i, message in enumerate(messages, 1):
        message = message.strip()
        if not message:
            continue
        pred = analyze_message(model, message)
        print(f"{Fore.YELLOW}{i}. {Fore.WHITE}{message}\n   النتيجة: {label_map.get(pred, Fore.LIGHTBLACK_EX + '🔘 غير معروف')}\n")

def run_analysis():
    show_welcome()
    print_start_time()
    model = load_model()

    while True:
        print(Fore.BLUE + "اختر نوع التحليل:\n1. رسالة واحدة\n2. ملف رسائل\n3. خروج")
        choice = input("> ").strip()
        
        if choice == "1":
            test_message = input(Fore.CYAN + "📩 أدخل الرسالة لتحليلها:\n> ")
            prediction = analyze_message(model, test_message)
            label_map = {
                "safe": Fore.GREEN + "✅ لا يوجد تهديد.",
                "phishing": Fore.RED + "⚠ الرسالة تبدو كعملية احتيال.",
                "http": Fore.MAGENTA + "🚨 تحتوي على رابط مشبوه."
            }
            print(Fore.CYAN + "\n🔍 تم تحليل الرسالة. النتيجة:")
            print(label_map.get(prediction, Fore.YELLOW + "🔘 لم يتم التعرف على نوع الرسالة.\n"))
        
        elif choice == "2":
            filepath = input(Fore.CYAN + "📂 أدخل مسار ملف الرسائل (مثال: data/bulk_messages.txt):\n> ")
            analyze_file(model, filepath)
        
        elif choice == "3":
            print(Fore.GREEN + "👋 شكراً لاستخدامك FamilySec System. مع السلامة!")
            break
        
        else:
            print(Fore.RED + "❌ اختيار غير صالح، يرجى المحاولة مجدداً.\n")

if __name__ == "__main__":
    run_analysis()
