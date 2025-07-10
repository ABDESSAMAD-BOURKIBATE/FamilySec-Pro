from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

from app.detector import load_model, analyze_message

app = Flask(__name__)
app.secret_key = 'secret_key_abdessamad_2025'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'alerts.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    level = db.Column(db.String(20), nullable=False)

model = load_model()

@app.before_request
def create_tables_if_not_exist():
    if not hasattr(app, 'tables_created'):
        db.create_all()
        app.tables_created = True

@app.route("/")
def index():
    alerts = Alert.query.all()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_year = datetime.now().year
    developer_info = {
        "name": "عبد الصمد بوركيبات",
        "version": "1.0",
        "license": "MIT License"
    }
    return render_template(
        "index.html",
        alerts=alerts,
        current_time=current_time,
        current_year=current_year,
        dev=developer_info
    )

@app.route("/add", methods=["POST"])
def add_alert():
    msg = request.form.get("message", "").strip()
    level = request.form.get("level", "").strip()
    if not msg or level not in ("safe", "phishing", "http"):
        flash("❌ بيانات غير صحيحة. حاول مجددا.", "danger")
        return redirect(url_for("index"))
    new_alert = Alert(message=msg, level=level)
    db.session.add(new_alert)
    db.session.commit()
    flash("✅ تم إضافة التنبيه بنجاح.", "success")
    return redirect(url_for("index"))

@app.route("/delete/<int:alert_id>")
def delete_alert(alert_id):
    alert = Alert.query.get_or_404(alert_id)
    db.session.delete(alert)
    db.session.commit()
    flash("✅ تم حذف التنبيه بنجاح.", "success")
    return redirect(url_for("index"))

@app.route("/analyze", methods=["POST"])
def analyze():
    msg = request.form.get("message_to_analyze", "").strip()
    if not msg:
        flash("❌ لا يمكن تحليل رسالة فارغة.", "danger")
        return redirect(url_for("index"))
    level = analyze_message(model, msg)
    new_alert = Alert(message=msg, level=level)
    db.session.add(new_alert)
    db.session.commit()
    flash(f"🔍 تم تحليل الرسالة. النتيجة: {level}", "info")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
