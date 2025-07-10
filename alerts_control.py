import json
import os

DATA_FILE = "alerts.json"

# تحميل التنبيهات من ملف JSON أو إنشاء قائمة فارغة
def load_alerts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# حفظ التنبيهات في ملف JSON
def save_alerts(alerts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(alerts, f, ensure_ascii=False, indent=2)

# عرض التنبيهات بشكل مرتب
def show_alerts(alerts):
    if not alerts:
        print("\n⚠️ لا توجد تنبيهات حالياً.\n")
        return
    print("\n📋 قائمة التنبيهات\n")
    print(f"{'رقم':<4} {'الرسالة':<50} {'المستوى':<10}")
    print("-" * 70)
    for alert in alerts:
        msg = alert['message']
        if len(msg) > 47:
            msg = msg[:44] + "..."
        print(f"{alert['id']:<4} {msg:<50} {alert['level']:<10}")
    print()

# إضافة تنبيه جديد
def add_alert(alerts):
    msg = input("📝 أدخل نص الرسالة:\n> ").strip()
    if not msg:
        print("❌ لا يمكن أن تكون الرسالة فارغة.")
        return
    level = input("⚠️ اختر المستوى (safe, phishing, http):\n> ").strip().lower()
    if level not in ("safe", "phishing", "http"):
        print("❌ مستوى غير صالح.")
        return
    new_id = max((alert['id'] for alert in alerts), default=0) + 1
    alerts.append({"id": new_id, "message": msg, "level": level})
    save_alerts(alerts)
    print(f"✅ تم إضافة التنبيه رقم {new_id}.")

# حذف تنبيه
def delete_alert(alerts):
    try:
        del_id = int(input("🗑️ أدخل رقم التنبيه للحذف:\n> ").strip())
    except ValueError:
        print("❌ الرقم غير صحيح.")
        return
    new_alerts = [alert for alert in alerts if alert['id'] != del_id]
    if len(new_alerts) == len(alerts):
        print(f"❌ لم يتم العثور على تنبيه بالرقم {del_id}.")
    else:
        save_alerts(new_alerts)
        alerts[:] = new_alerts  # حدّث القائمة الأصلية
        print(f"✅ تم حذف التنبيه رقم {del_id}.")

# القائمة الرئيسية للوحة التحكم
def control_panel():
    alerts = load_alerts()
    while True:
        print("\n=== لوحة تحكم FamilySec-Pro | تنبيهات الرسائل ===")
        print("1. عرض التنبيهات")
        print("2. إضافة تنبيه جديد")
        print("3. حذف تنبيه")
        print("4. خروج")
        choice = input("> ").strip()
        if choice == '1':
            show_alerts(alerts)
        elif choice == '2':
            add_alert(alerts)
        elif choice == '3':
            delete_alert(alerts)
        elif choice == '4':
            print("👋 شكراً لاستخدامك النظام. إلى اللقاء!")
            break
        else:
            print("❌ اختيار غير صالح، حاول مرة أخرى.")

if __name__ == "__main__":
    control_panel()
