from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponse,JsonResponse
import json
import sys
sys.path.append(r'E:\All Projects\Web Project\Blood\Blood_app')
from country import country_data
# Create your views here.
# print('Saboj')
# print(country_data)
def home_page(request):

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

        Person.objects.create(
            name = name,
            age = age,
            blood_group = blood_group,
            mobile_number = mobile_number,
            division  = division ,
            district = district,
            subdistrict = subdistrict,
            lastdonate = lastdonate,
            person_image = person_image,
        )
        return redirect('home_page')
    
  
    context =  {
         'country': country_data,
      }
    
    return render(request , 'home_page.html',context)


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
       

