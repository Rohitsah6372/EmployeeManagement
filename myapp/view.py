from django.http import HttpResponse
from django.shortcuts import render
import datetime as d

def home(request):
    check = None  # Default value

    if request.method == 'POST':
        check = request.POST.get('check', '')  # Use get() to avoid KeyError
        print(check)  # Debugging print statement
    
    print("Test function is called from view")
    date = d.datetime.now()

    return render(request, "home.html", {"check": check, "date": date})

def about(request):
    print("Test function is called from view")
    date = d.datetime.now()
    return render(request, "about.html", {"date": date})

def services(request):
    print("Test function is called from view")
    date = d.datetime.now()
    return render(request, "services.html", {"date": date})
