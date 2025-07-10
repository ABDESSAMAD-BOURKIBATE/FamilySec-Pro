from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = "data/alerts.json"

def load_alerts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_alerts(alerts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(alerts, f, ensure_ascii=False, indent=2)

alerts = load_alerts()

@app.route("/", methods=["GET"])
def home():
    return render_template("dashboard.html", alerts=alerts)

@app.route("/add_alert", methods=["POST"])
def add_alert():
    message = request.form.get("message")
    level = request.form.get("level")
    if message and level:
        new_id = max([alert["id"] for alert in alerts], default=0) + 1
        alerts.append({"id": new_id, "message": message, "level": level})
        save_alerts(alerts)
    return redirect(url_for("home"))

@app.route("/delete_alert", methods=["POST"])
def delete_alert():
    alert_id = request.form.get("id")
    if alert_id:
        alert_id = int(alert_id)
        global alerts
        alerts = [alert for alert in alerts if alert["id"] != alert_id]
        save_alerts(alerts)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
