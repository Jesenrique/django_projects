from django.contrib import admin
from .models import categorie,post

# Register your models here.
class adminblog (admin.ModelAdmin):
    readonly_fields=("created", "updated")

class adminpost (admin.ModelAdmin):
    readonly_fields=("created", "updated")


admin.site.register(categorie,adminblog)
admin.site.register(post,adminpost)
