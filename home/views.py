from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
  
# Create your views here.
def HomeView(request):
      
    # render function takes argument  - request
    # and return HTML as response

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {

        'num_visits': num_visits,
    }

    return render(request, "home/home.html", context=context)