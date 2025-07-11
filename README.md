
# 🛡️ FamilySec-Pro

**AI-Powered Cybersecurity for Families**  
**الحماية السيبرانية للأسرة عبر الذكاء الاصطناعي**

---

## 🧭 الفكرة العامة | General Idea

`FamilySec-Pro` هو نظام ذكي يساعد الأسر على اكتشاف الرسائل الضارة، الروابط المشبوهة، ومحاولات التصيد (Phishing) التي قد تهدد سلامة الأطفال أو الوالدين داخل الفضاء الرقمي.  
يعتمد النظام على تحليل المحتوى، تقديم إنذارات فورية، وتخزين السجلات في قاعدة بيانات محلية.

**FamilySec-Pro** is a smart detection system for phishing, malicious links, and harmful messages that might compromise digital safety in families. It uses AI-powered analysis, alerts, and logs to empower secure digital parenting.

---

## 🎯 الفئة المستهدفة | Target Audience

- أولياء الأمور الباحثون عن حماية رقمية لأبنائهم  
- المعلمون والمربون المهتمون بسلامة البيئة التعليمية الرقمية  
- المؤسسات التربوية والرعوية  
- الجمعيات المهتمة بحقوق الطفل في العالم الرقمي  
- الباحثون في الأمن السيبراني الأخلاقي

---

## ⚖️ الشق القانوني | Legal Framework

### 🇲🇦 بالعربية:
يراعي هذا المشروع المقتضيات القانونية المتعلقة بحماية المعطيات الشخصية (مثل قانون 09.08 في المغرب)، ومبادئ الأمن الرقمي الأسري. لا يقوم المشروع بجمع أي بيانات حساسة، ويعتمد على تخزين محلي وآليات غير متصلة (Offline First).

### 🌍 In English:
This project respects data protection laws (e.g., GDPR, Moroccan Law 09.08) and promotes digital safety within families. It avoids any cloud-based storage and ensures all processing is local, reinforcing privacy-first principles.

---

## 🚀 المميزات | Features

- 🔎 كشف التصيد والروابط الضارة  
- 🧠 تحليل ذكي وتقييم درجة التهديد  
- 📊 إشعارات وتنبيهات فورية  
- 💾 تخزين السجلات محليًا (JSON + SQLite)  
- 🧩 واجهة قابلة للتطوير (Dashboard قيد الإعداد)  

---

## 🛠️ التثبيت والتشغيل | Installation

```bash
# استنساخ المستودع
git clone https://github.com/ABDESSAMAD-BOURKIBATE/FamilySec-Pro.git
cd FamilySec-Pro

# إنشاء بيئة افتراضية
python3 -m venv venv
source venv/bin/activate

# تثبيت التبعيات
pip install -r requirements.txt

# تشغيل المشروع
python run.py


---

🔬 خارطة التطوير | Development Roadmap

✅ تنبيهات أساسية وتحليل النصوص

✅ تخزين داخلي مزدوج (JSON + SQLite)

⏳ واجهة مرئية عبر Flask أو Streamlit

⏳ دعم لغات متعددة (عربية، إنجليزية، فرنسية)

⏳ تكامل مع Telegram/WhatsApp API

⏳ نظام صلاحيات للأبناء والآباء



---

🧪 الاستخدام | Usage

قم بتشغيل run.py لتفعيل نظام المراقبة.

تحقق من alerts.json و alerts.db للاطلاع على السجلات.

عدّل قواعد التحليل والتنبيه من داخل alerts_control.py حسب احتياجك.



---

📌 حالات الاستخدام | Use Cases

الحالة	النتيجة

طفل يتلقى رابطًا غريبًا	⚠️ تحذير من التصيد
تهديد لفظي أو تنمّر	🚨 رسالة خطيرة
رابط تعليمي موثوق	✅ آمن



---

📜 الترخيص | License

تم تطوير هذا المشروع بغرض البحث الأكاديمي والتربوي فقط.
يُسمح بالاستخدام الشخصي أو التربوي دون قيود، ويمنع إعادة توزيعه تجاريًا بدون إذن خطي.

الاسم الكامل: عبد الصمد بوركيبات
التوقيع: Bourkibate.A
البريد الإلكتروني: bourkibate@gmail.com
السنة: 2025

> 💬 "الأمن الرقمي ليس رفاهية، بل ضرورة تربوية لكل أسرة واعية."




