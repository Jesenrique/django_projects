from django.urls import path
from carApp.views import clean_car,agregate_product,eliminate_product,substract_product


# Variable usada para llamar mejor a las url sin quivocarse con otras apps
app_name="car"

urlpatterns = [
    path('agregate/<int:product_id>', agregate_product, name='agregate'),
    path('eliminate/', eliminate_product, name='eliminate'),
    path('substract/<int:product_id>', substract_product, name='substract'),
    path('clean/', clean_car, name='clean'),
]
