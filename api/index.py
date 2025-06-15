import os
import sys
from django.core.wsgi import get_wsgi_application

# Set project path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Assignment1.settings")

# WSGI app for Vercel
app = get_wsgi_application()

def handler(environ, start_response):
    return app(environ, start_response)
