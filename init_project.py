import os

project_root = os.getcwd()
structure = {
    "app": ["detector.py", "analyzer.py", "legal_engine.py", "alerts.py", "dashboard.py"],
    "data": ["samples/.keep"],
    "scripts": ["run_familysec.sh"],
    "tests": ["unit_tests.py"],
    "": ["requirements.txt", "run.py", "README.md"]
}

for folder, files in structure.items():
    dir_path = os.path.join(project_root, folder)
    os.makedirs(dir_path, exist_ok=True)
    for file in files:
        file_path = os.path.join(dir_path, file)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        open(file_path, 'a').close()

