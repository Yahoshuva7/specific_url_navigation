from django.shortcuts import render

# Create your views here.
def tiffin(request):
    return render(request,'food.html')

def biriyani(request):
    return render(request,'biriyani.html')