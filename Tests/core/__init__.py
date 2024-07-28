# __init__.py
import os

# Initialize Firebase
if os.getenv('DJANGO_SETTINGS_MODULE') == 'your_project.settings':
    from .firebase_config import *
