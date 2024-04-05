from django.urls import path
from food.views import *
app_name='food'
urlpatterns=[
    path('tiffin/',tiffin,name='tiffin'),
    path('biriyani/',biriyani,name='biriyani'),
]