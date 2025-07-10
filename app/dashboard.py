from flask import Flask, render_template, request, redirect, url_for, make_response
import json
import os
from weasyprint import HTML

app = Flask(__name__)

# مسار ملف التنبيهات
DATA_FILE = "data/alerts.json"

# تحميل التنبيهات من الملف
def load_alerts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# حفظ التنبيهات إلى الملف
def save_alerts(alerts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(alerts, f, ensure_ascii=False, indent=2)

# تحميل التنبيهات عند التشغيل
alerts = load_alerts()

# الصفحة الرئيسية
@app.route("/", methods=["GET"])
def home():
    return render_template("dashboard.html", alerts=alerts)

# إضافة تنبيه جديد
@app.route("/add_alert", methods=["POST"])
def add_alert():
    message = request.form.get("message")
    level = request.form.get("level")
    if message and level:
        new_id = max([alert["id"] for alert in alerts], default=0) + 1
        alerts.append({"id": new_id, "message": message, "level": level})
        save_alerts(alerts)
    return redirect(url_for("home"))

# حذف تنبيه معين
@app.route("/delete_alert", methods=["POST"])
def delete_alert():
    alert_id = request.form.get("id")
    if alert_id:
        alert_id = int(alert_id)
        global alerts
        alerts = [alert for alert in alerts if alert["id"] != alert_id]
        save_alerts(alerts)
    return redirect(url_for("home"))

# حذف جميع التنبيهات
@app.route("/clear_alerts", methods=["POST"])
def clear_alerts():
    global alerts
    alerts = []
    save_alerts(alerts)
    return redirect(url_for("home"))

# صفحة تحليل النصوص
@app.route("/analyze", methods=["GET", "POST"])
def analyze():
    result = None
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            result = {
                "original_text": text,
                "word_count": len(text.split()),
                "char_count": len(text),
                "upper_text": text.upper()
            }
    return render_template("analyze.html", result=result)

# تصدير تقرير PDF من التنبيهات
@app.route("/export_pdf")
def export_pdf():
    rendered = render_template("dashboard.html", alerts=alerts)
    pdf = HTML(string=rendered).write_pdf()
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=alerts_report.pdf'
    return response

# تشغيل السيرفر
if __name__ == "__main__":
    app.run(debug=True)
