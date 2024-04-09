cd back-end
// TERMINAL powershell --> CREATE VIRTUAL ENVIRONMENT
python -m venv .venv
// TERMINAL Git Bash --> ACTIVATE VIRTUAL ENVIRONMENT
. .venv/Scripts/activate
// INSTALL REQUIREMENTS
pip freeze > requirements.txt
pip install -r requirements.txt
// EXECUTE API
python \src\\main.py
// DEACTIVATE VIRTUAL ENVIRONMENT
deactivate