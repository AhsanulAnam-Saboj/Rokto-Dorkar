from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib import messages
from math import radians, sin, cos, sqrt, atan2
import json
import sys
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from datetime import timedelta
import random
import requests
from Blood_app.country import country_data
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login

User = get_user_model()

def login(request):

    if request.method == "POST":
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        if not User.objects.filter(phone_number=phone_number).exists():
            messages.info(request,'User not exist')
            return redirect('login')
        
        user = authenticate(phone_number = phone_number,password = password)
        # print('Kortamni')
        if user is None:
            messages.info(request,'Invalid Password')
            return redirect('login')
        else:
            auth_login(request,user)
            return redirect('home')


    return render(request,'login.html')



def logout(request):
    auth_logout(request)  # Use Django's logout function
    return redirect('login')  # Or wherever you want to redirect after logout
    


def signup(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        user = User.objects.filter(phone_number = phone_number)
        if user.exists():
            messages.info(request,'Phone number already exists')
            return redirect('signup')
        user = User.objects.create(
            phone_number = phone_number
        )
        user.set_password(password)
        user.save()
        messages.info(request,'User created successfully')
        return redirect('login')
    
    return render(request,'signup.html')



def get_lat_lon(address):
    url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json"
    headers = {"User-Agent": "MyGeocodingApp/1.0 (ahsanulanamsaboj1999@gmail.com)"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)  # Timeout added
        # print(address)
        # print(response)
        # print(f"Status Code: {response.status_code}")  # Debugging
        # print(f"Response Text: {response.text}")  # Debugging
        
        if response.status_code == 200 and response.text.strip():
            data = response.json()
            # print(data)
            if data:
                return data[0]["lat"], data[0]["lon"]
            else:
                return None,None
        else:
            return None,None

    except requests.exceptions.Timeout:
        return None,None
    except requests.exceptions.RequestException as e:
        return None,None


def haversine(lat1, lon1, lat2, lon2):

    # print(lat1,lat2,lon1,lon2)
    if None in [lat1, lon1, lat2, lon2]:
        return 100000000
    # Radius of the Earth in km
    R = 6371.0
    
    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    # Distance in kilometers
    distance = R * c
    return distance


@login_required(login_url="/login")
def profile(request):
    
    person,created = Person.objects.get_or_create(user=request.user)
    if request.method =="POST":
        data = request.POST
        person_image = request.FILES.get('person_image')
        name = data.get('name')
        age =  data.get('age')
        mobile_number = data.get('mobile_number')
        blood_group = data.get('blood_group')
        division  =  data.get('division')
        district =  data.get('district')
        subdistrict =  data.get('subdistrict')
        lastdonate =  data.get('lastdonate')
        address = f"{subdistrict}, {district}, {division}"
        latitude , longitude = get_lat_lon(address)
        # print({latitude} + {longitude} + "saboj")
        if person_image:
          person.person_image = person_image
        person.name = name
        person.age = age
        person.mobile_number = mobile_number
        person.blood_group = blood_group
        person.division = division
        person.district = district
        person.subdistrict = subdistrict
        person.lastdonate = lastdonate
        person.longitude = longitude
        person.latitude = latitude
        person.save()

        return redirect('profile')
    
  
    context =  {
         'country': country_data,
         'person': person,
      }
    
    return render(request , 'profile.html',context)

@login_required(login_url="/login")
def home(request):
    queryset = Person.objects.all().order_by('-id')[:200]
    
    # print(queryset)
    if request.method == "POST":
        data = request.POST
        blood_group = data.get('blood_group')
        division = data.get('division')
        district = data.get('district')
        subdistrict = data.get('subdistrict')
        address = f"{subdistrict},{district},{division}"
        
        latitude , longitude = get_lat_lon(address)
        # print(str(latitude) + str(longitude) + "saboj")


        filters = {}
        
        # Apply filters based on provided input
        if blood_group:
            filters['blood_group'] = blood_group
        
        # print(blood_group)
        # print(latitude, longitude)
        # Filter people who donated at least 4 months ago
        filters['lastdonate__lte'] = timezone.now().date() - relativedelta(days=4*30)
        filtered_ids = Person.objects.filter(**filters).values_list('id', flat=True)
        
        # Shuffle and limit to 200 people
        filtered_persons = Person.objects.filter(id__in=filtered_ids)
        # random.shuffle(filtered_persons)
        queryset = []
        for invidual in filtered_persons:
            print(latitude, invidual.latitude)
            if None in [latitude, longitude, invidual.latitude, invidual.longitude]:
                continue
            distance = haversine(float(latitude), float(longitude), float(invidual.latitude), float(invidual.longitude))
            if distance <= 30:
             queryset.append(invidual)
    
    # print(queryset)
    context = {'person': queryset, 'country': country_data}
    return render(request, 'home.html', context)
       

def about(request):
    
    return render(request,'about.html')