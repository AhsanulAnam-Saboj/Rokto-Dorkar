"""
URL configuration for Blood project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Import views from the Blood_app
from Blood_app.views import profile, home,login,signup,logout,about

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    
    # Application URLs
    path('profile/', profile, name='profile'),
    path('home/', home, name='home'),
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),
    path('signup/',signup,name="signup"),
    path('about/',about,name='about')
    
]

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serving static files
urlpatterns += staticfiles_urlpatterns()
