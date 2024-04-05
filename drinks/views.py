from django.shortcuts import render

# Create your views here.
def drink(request):
    return render(request,'drinks.html')