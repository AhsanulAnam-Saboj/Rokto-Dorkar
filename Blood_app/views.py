from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponse,JsonResponse
import json
import sys
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
sys.path.append(r'E:\All Projects\Web Project\Blood\Blood_app')
from country import country_data

User = get_user_model()
def login_page(request):

    return render(request,'login_page.html')

def registration_page(request):

    return render(request,'registration_page.html')

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
        # print(person_image)
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
      }
    
    return render(request , 'account_page.html',context)


def main_page(request):
    
    queryset = Person.objects.all()
    
    if request.method == "POST":
        data = request.POST
        blood_group = data.get('blood_group')
        division = data.get('division')
        district = data.get('district')
        subdistrict = data.get('subdistrict')
        
        # print(blood_group)
        # print(division)
        # print(district)
        
        if blood_group:
            queryset = queryset.filter(blood_group__icontains=blood_group)
        if division:
            queryset = queryset.filter(division__icontains=division)
        if district:
            queryset = queryset.filter(district__icontains=district)
        if subdistrict:
            queryset = queryset.filter(subdistrict__icontains=subdistrict)
        

    print(queryset)
    context = {'person': queryset, 'country': country_data}
    return render(request, 'main_page.html', context)
       


