from django.contrib import admin
from .models import services

# Register your models here.

class adminServices(admin.ModelAdmin):
    readonly_fields=("created", "updated")
    
admin.site.register(services, adminServices)