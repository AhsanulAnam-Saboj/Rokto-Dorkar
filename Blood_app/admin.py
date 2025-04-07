from django.contrib import admin

# Register your models here.
from .models import Person,User


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'mobile_number', 'person_image','blood_group', 'division', 'district', 'subdistrict', 'lastdonate','longitude','latitude')


admin.site.register(Person, PersonAdmin)
admin.site.register(User)