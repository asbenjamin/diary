from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
  
# Create your views here.
def HomeView(request):
      
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "home/home.html")