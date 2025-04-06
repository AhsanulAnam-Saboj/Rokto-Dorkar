import os
import django
from django.core.management import call_command
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Blood.settings")
django.setup()

# Provide the superuser credentials
username = '01739640467'
password = '1999@saboj'

try:
    # Try to get the user; if it exists, do nothing
    from django.contrib.auth.models import User
    if not User.objects.filter(username=username).exists():
        # Create the superuser if it doesn't exist
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superuser created successfully.")
    else:
        print("Superuser already exists.")
except Exception as e:
    print(f"Error creating superuser: {str(e)}")
