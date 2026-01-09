"""
Configuration settings for the Waste Classification API
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

# Flask Configuration
FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')
FLASK_PORT = int(os.getenv('FLASK_PORT', 5000))
FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

# File Upload Configuration
UPLOAD_FOLDER = BASE_DIR / 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

# Model Configuration
MODEL_FOLDER = BASE_DIR / 'models'
MODEL_FILENAME = 'RF_Classifier.pkl'
MODEL_PATH = MODEL_FOLDER / MODEL_FILENAME

# Categories
CATEGORIES = {0: 'ORGANIC', 1: 'NONORGANIC'}

# CORS Configuration
CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*').split(',')

# Logging Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
