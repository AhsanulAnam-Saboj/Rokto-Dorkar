import os
import django
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.conf import settings

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Blood.settings")
django.setup()

# Superuser credentials
username = '01739640467'
email = 'ahsanulanamsaboj1999@gmail.com'
password = '1999s@boj'

try:
    User = get_user_model()  # This will get your custom user model if you have one
    
    if not User.objects.filter(username=username).exists():
        # Create the superuser
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"Superuser '{username}' created successfully.")
    else:
        print(f"Superuser '{username}' already exists.")
        
except Exception as e:
    print(f"Error creating superuser: {str(e)}")