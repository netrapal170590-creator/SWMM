"""Simple environment-based test configuration."""

import os


BASE_URL = os.getenv("BASE_URL", "http://172.16.40.162/landing").rstrip("/")
USERNAME = os.getenv("APP_USERNAME", "ADMIN")
PASSWORD = os.getenv("APP_PASSWORD", "")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
