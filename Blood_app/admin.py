from django.contrib import admin

# Register your models here.
from .models import Person,User


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'mobile_number', 'blood_group', 'division', 'district', 'subdistrict', 'lastdonate')


admin.site.register(Person, PersonAdmin)
admin.site.register(User)