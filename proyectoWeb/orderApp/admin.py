from django.contrib import admin
from .models import TableOrder, Order

# Register your models here.
admin.site.register([Order,TableOrder])