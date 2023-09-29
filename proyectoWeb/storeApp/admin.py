from django.contrib import admin
from .models import categorieProduct, product

# Register your models here.
class adminCategorieProduct(admin.ModelAdmin):
    readonly_fields=("created", "updated")

class adminProduct(admin.ModelAdmin):
    readonly_fields=("created", "updated")

admin.site.register(categorieProduct, adminCategorieProduct)
admin.site.register(product, adminProduct)