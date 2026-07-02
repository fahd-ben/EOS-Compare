import sys
import os

# Permet d'importer app.py qui se trouve a la racine du projet
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import app  # noqa: E402  (app = create_app() dans app.py)

# Vercel (runtime @vercel/python) cherche un objet WSGI nomme "app"
