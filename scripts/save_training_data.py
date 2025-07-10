import os
import csv
from collections import Counter

TRAIN_FILE = "data/train_messages.csv"
FIELDNAMES = ["message", "label"]

def initialize_training_file():
    """إنشاء ملف التدريب إذا لم يكن موجودًا مع رؤوس الأعمدة"""
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.isfile(TRAIN_FILE):
        with open(TRAIN_FILE, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
        print(f"تم إنشاء ملف التدريب الجديد: {TRAIN_FILE}")

def add_training_message(message: str, label: str):
    """إضافة رسالة جديدة مع تصنيفها إلى ملف التدريب"""
    if label not in ["safe", "phishing", "http"]:
        raise ValueError(f"التصنيف '{label}' غير مدعوم. استخدم: safe, phishing, http")
    with open(TRAIN_FILE, mode='a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow({"message": message, "label": label})
    print(f"تمت إضافة الرسالة مع التصنيف '{label}'")

def get_training_summary():
    """عرض ملخص عن عدد الرسائل في كل تصنيف"""
    if not os.path.isfile(TRAIN_FILE):
        print("ملف التدريب غير موجود.")
        return
    counts = Counter()
    with open(TRAIN_FILE, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            counts[row["label"]] += 1
    print("ملخص بيانات التدريب:")
    for label, count in counts.items():
        print(f"  - {label}: {count} رسالة")

def main():
    initialize_training_file()
    while True:
        print("\nاختر خيارًا:\n1. إضافة رسالة تدريب جديدة\n2. عرض ملخص بيانات التدريب\n3. خروج")
        choice = input("> ").strip()
        if choice == "1":
            msg = input("أدخل نص الرسالة:\n> ").strip()
            lbl = input("أدخل التصنيف (safe, phishing, http):\n> ").strip().lower()
            try:
                add_training_message(msg, lbl)
            except ValueError as e:
                print(f"خطأ: {e}")
        elif choice == "2":
            get_training_summary()
        elif choice == "3":
            print("تم الخروج. حفظت التغييرات.")
            break
        else:
            print("خيار غير صحيح، حاول مجددًا.")

if __name__ == "__main__":
    main()
