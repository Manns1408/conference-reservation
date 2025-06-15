import sys
import os
from django.core.wsgi import get_wsgi_application

# Set settings path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Assignment1.settings")

# Load application
application = get_wsgi_application()

# Vercel will call this
def handler(environ, start_response):
    return application(environ, start_response)
