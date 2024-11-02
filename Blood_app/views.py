from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib import messages
import json
import sys
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
import random
sys.path.append(r'E:\All Projects\Web Project\Rokto Dorkar\Blood_app')
from country import country_data

User = get_user_model()

def login_page(request):

    if request.method == "POST":
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        if not User.objects.filter(phone_number=phone_number).exists():
            messages.info(request,'User not exist')
            return redirect('login_page')
        
        user = authenticate(phone_number = phone_number,password = password)
        # print('Kortamni')
        if user is None:
            messages.info(request,'Invalid Password')
            return redirect('login_page')
        else:
            login(request,user)
            return redirect('main_page')


    return render(request,'login_page.html')

def logout_page(request):

    logout(request)
    return redirect('login_page')
    


def registration_page(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        user = User.objects.filter(phone_number = phone_number)
        if user.exists():
            messages.info(request,'Phone number already exists')
            return redirect('registration_page')
        user = User.objects.create(
            phone_number = phone_number
        )
        user.set_password(password)
        user.save()
        messages.info(request,'User created successfully')
        return redirect('login_page')
        
    return render(request,'registration_page.html')

@login_required(login_url="/login_page")
def account_page(request):
    
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
        person.save()

        return redirect('account_page')
    
  
    context =  {
         'country': country_data,
         'person': person,
      }
    
    return render(request , 'account_page.html',context)

@login_required(login_url="/login_page")
def main_page(request):
    queryset = Person.objects.all().order_by('-id')[:200]
    
    print(queryset)
    if request.method == "POST":
        data = request.POST
        blood_group = data.get('blood_group')
        division = data.get('division')
        district = data.get('district')
        subdistrict = data.get('subdistrict')
        
        filters = {}
        
        # Apply filters based on provided input
        if blood_group:
            filters['blood_group'] = blood_group
        if division != "ALL":
            filters['division'] = division
        if district != "ALL":
            filters['district'] = district
        if subdistrict != "ALL":
            filters['subdistrict'] = subdistrict
        print(blood_group)
        # Filter people who donated at least 4 months ago
        filters['lastdonate__lte'] = timezone.now().date() - timedelta(days=4*30)
        filtered_ids = Person.objects.filter(**filters).values_list('id', flat=True)
        
        # Shuffle and limit to 200 people
        filtered_ids = random.sample(list(filtered_ids), min(200, len(filtered_ids)))
        queryset = Person.objects.filter(id__in=filtered_ids)

    context = {'person': queryset, 'country': country_data}
    return render(request, 'main_page.html', context)
       
