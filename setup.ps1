Remove-Item venv -Recurse -ErrorAction Ignore
Remove-Item __pycache__ -Recurse -ErrorAction Ignore
python -m venv venv
& .\venv\Scripts\Activate.ps1
pip install -r requirements.txt