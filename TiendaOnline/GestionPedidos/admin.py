from django.contrib import admin
from GestionPedidos.models import Article, Clientes, Order


class Articleadmin(admin.ModelAdmin):
    list_display=("name","price")
    search_fields=("name","price")
    list_filter=("price",)

class Orderadmin(admin.ModelAdmin):
    list_display=("number","date")
    list_filter=("date",)
    date_hierarchy=("date")
# Register your models here.
admin.site.register(Article,Articleadmin)

#de esta manera se agregamos clientes a admin para que
#realice información sobre la tabla 
admin.site.register(Clientes)

admin.site.register(Order,Orderadmin)