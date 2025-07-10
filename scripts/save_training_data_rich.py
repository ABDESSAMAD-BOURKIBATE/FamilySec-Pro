import os
import csv
from collections import Counter
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.align import Align

console = Console()

TRAIN_FILE = "data/train_messages.csv"
LOG_FILE = "data/change_log.txt"
FIELDNAMES = ["message", "label"]
PASSWORD = "MySecurePass2025"  # غيّرها لكلمة مرورك

def init_files():
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.isfile(TRAIN_FILE):
        with open(TRAIN_FILE, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
    if not os.path.isfile(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("سجل تغييرات تدريب FamilySec-Pro\n========================================\n\n")

def authenticate():
    console.print(Panel.fit("[bold red]🔐 أدخل كلمة المرور لتشغيل النظام[/bold red]\n(محمية بواسطة Pr. ABDESSAMAD BOURKIBATE)", style="yellow"))
    for _ in range(3):
        pwd = Prompt.ask("كلمة المرور", password=True)
        if pwd == PASSWORD:
            return True
        else:
            console.print("[red]كلمة المرور خاطئة، حاول مجددًا.[/red]")
    console.print("[bold red]تم رفض الدخول بعد 3 محاولات.[/bold red]")
    return False

def log_change(action, message, label=""):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{now} - {action}: '{message}' تصنيف: {label}\n")

def add_training_message():
    console.print(Panel.fit("📝 [bold green]إضافة رسالة تدريب جديدة[/bold green]", style="cyan"))
    msg = Prompt.ask("أدخل نص الرسالة").strip()
    label = Prompt.ask("أدخل التصنيف (safe, phishing, http)").strip().lower()
    if label not in ["safe", "phishing", "http"]:
        console.print("[red]خطأ: التصنيف غير صحيح. يجب أن يكون أحد هذه: safe, phishing, http[/red]")
        return
    with open(TRAIN_FILE, mode='a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow({"message": msg, "label": label})
    log_change("إضافة رسالة تدريب", msg, label)
    console.print("[bold green]تمت إضافة الرسالة والتصنيف بنجاح![/bold green]")

def show_summary():
    if not os.path.isfile(TRAIN_FILE):
        console.print("[red]ملف التدريب غير موجود.[/red]")
        return
    counts = Counter()
    with open(TRAIN_FILE, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            counts[row["label"]] += 1
    table = Table(title="📊 ملخص بيانات التدريب", style="bold cyan")
    table.add_column("التصنيف", style="magenta", justify="center")
    table.add_column("عدد الرسائل", style="green", justify="center")
    for label, count in counts.items():
        table.add_row(label, str(count))
    console.print(table)

def show_log():
    if not os.path.isfile(LOG_FILE):
        console.print("[red]سجل التغييرات غير موجود.[/red]")
        return
    console.print(Panel.fit("📜 [bold blue]سجل التغييرات[/bold blue]", style="bright_blue"))
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    console.print(Align.left(Text(content, style="white")))

def main_menu():
    while True:
        header = Panel(
            f"مرحبًا بك في نظام إدارة بيانات التدريب\n"
            f"🚀 مشروع FamilySec-Pro\n"
            f"توقيع: [bold yellow]Abdessamad BOURKIBATE[/bold yellow] | تاريخ: {datetime.now().strftime('%Y-%m-%d')}",
            style="bold magenta",
            expand=False,
            padding=(1,2),
        )
        console.print(header)

        console.print("اختر خيارًا:\n[1] إضافة رسالة تدريب جديدة\n[2] عرض ملخص بيانات التدريب\n[3] عرض سجل التغييرات\n[4] خروج")
        choice = Prompt.ask("> [1/2/3/4]").strip()

        if choice == "1":
            add_training_message()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            show_log()
        elif choice == "4":
            console.print("[bold green]شكراً لاستخدامك النظام. إلى اللقاء![/bold green]")
            break
        else:
            console.print("[red]خيار غير صحيح، حاول مجددًا.[/red]")
        console.print("-" * 60)

if __name__ == "__main__":
    init_files()
    if authenticate():
        main_menu()
