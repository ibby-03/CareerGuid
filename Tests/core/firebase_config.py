# firebase_config.py
import firebase_admin
from firebase_admin import credentials

# Path to the downloaded service account key JSON file
cred = credentials.Certificate('config/serviceAccountKey.json')
firebase_admin.initialize_app(cred)
