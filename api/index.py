import sys
import os

from django.core.wsgi import get_wsgi_application

# Set the Django settings module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Assignment1.settings")

# Get the WSGI app
application = get_wsgi_application()

# Vercel expects this function
def handler(environ, start_response):
    return application(environ, start_response)
