

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

### بالعربية:
يراعي هذا المشروع المقتضيات القانونية المتعلقة بحماية المعطيات الشخصية (مثل قانون 09.08 في المغرب)، ومبادئ الأمن الرقمي الأسري. لا يقوم المشروع بجمع أي بيانات حساسة، ويعتمد على تخزين محلي وآليات غير متصلة (Offline First).

### In English:
This project respects data protection laws (e.g., GDPR, Moroccan Law 09.08) and promotes digital safety within families. It avoids any cloud-based storage and ensures all processing is local, reinforcing privacy-first principles.

---

## 🚀 المميزات | Features

- 🔎 كشف التصيد والروابط الضارة
- 🧠 تحليل ذكي وتقييم درجة التهديد
- 📊 إشعارات وتنبيهات فورية
- 💾 تخزين السجلات محليًا (JSON + SQLite)
- 🧩 واجهة قابلة للتطوير (Dashboard قيد الإعداد)

---

FamilySec-Pro/
├── app/                  # المنطق الرئيسي للتحليل والتنبيه
│   └── ...               # ملفات الذكاء الاصطناعي أو تحليل النصوص
├── data/                 # عينات البيانات أو الملفات المراقبة
│   └── alerts.json       # سجل تنبيهات بصيغة JSON
├── scripts/              # أدوات التثبيت أو التشغيل اليدوي
│   └── run_familysec.sh  # سكربت التشغيل
├── templates/            # قوالب الواجهة (إن وُجدت: HTML, Jinja2...)
├── tests/                # اختبارات التحقق من وحدات النظام
│   └── test_alerts.py    # مثال لاختبار التنبيهات
├── alerts.db             # قاعدة بيانات SQLite
├── alerts_control.py     # وحدة إدارة التنبيهات والتحذيرات
├── web_control.py        # وحدة إدارة التفاعل عبر الويب
├── init_project.py       # تهيئة المشروع لأول مرة
├── run.py                # الملف التنفيذي الرئيسي
├── requirements.txt      # قائمة التبعيات (المكتبات المطلوبة)
├── LICENSE               # الرخصة القانونية
└── README.md             # وثيقة التوثيق الرئيسية (هذا الملف)
---

## 🛠️ التثبيت والتشغيل | Installation

```bash
git clone https://github.com/ABDESSAMAD-BOURKIBATE/FamilySec-Pro.git
cd FamilySec-Pro
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py


---

🔬 خارطة التطوير | Development Roadmap

[x] تنبيهات أساسية وتحليل النصوص

[x] تخزين داخلي مزدوج (JSON + SQLite)

[ ] واجهة مرئية عبر Flask أو Streamlit

[ ] دعم لغات متعددة (عربية، إنجليزية، فرنسية)

[ ] تكامل مع Telegram/WhatsApp API

[ ] نظام صلاحيات للأبناء والآباء



---

🧪 الاستخدام | Usage

تشغيل run.py واختبار الرسائل

مراجعة alerts.json وalerts.db لتتبع الأحداث

تخصيص القواعد داخل alerts_control.py



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





