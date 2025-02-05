from django.contrib import admin

# Register your models here.
from .models import emp

class EmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'working', 'emp_id')

admin.site.register(emp)