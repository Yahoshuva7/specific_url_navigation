from django.urls import path
from drinks.views import *
app_name='drinks'
urlpatterns=[
    path('drink/',drink,name='drink'),
    
]
