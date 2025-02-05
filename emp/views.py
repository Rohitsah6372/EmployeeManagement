from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import emp

# Create your views here.
def emp_home(request):
    emps = emp.objects.all()



    return render(request, "emp/home.html", {
        'emps':emps
    })

def add_emp(request): 
    if request.method == "POST":
        # data fetch

        name = request.POST.get("name")
        emp_id = request.POST.get("emp_id")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        working = request.POST.get("working") == "on"  # Convert checkbox value to boolean
        department = request.POST.get("department")

        # create model object and set the data 
        e = emp()
        e.name = name
        e.emp_id = emp_id  # Corrected from e.id to e.emp_id
        e.phone = phone
        if e.working is None:
            e.working = False
        else:
            e.working = True
        e.department = department
        e.address = address

        # save the object
        e.save()
        
        print("Data is coming")
        return redirect('/emp/home/')
    
    return render(request, "emp/add_emp.html", {})



def delete_emp(request, id):
    e = emp.objects.get(pk = id)
    e.delete()
    print(id)
    return redirect("/emp/home/")


def update_emp(request, id):
    e = emp.objects.get(pk = id)
    return render(request, "emp/update.html", {
        'emp':e 
    })


def do_update(request, id):
    if request.method == 'POST':
        name = request.POST.get("name")
        emp_id = request.POST.get("emp_id")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        working = request.POST.get("working") == "on"  # Convert checkbox value to boolean
        department = request.POST.get("department")

    e = emp.objects.get(pk = id)
    e = emp()
    e.name = name
    e.emp_id = emp_id  # Corrected from e.id to e.emp_id
    e.phone = phone
    if e.working is None:
        e.working = False
    else:
        e.working = True
    e.working = working
    e.department = department
    e.address = address

    # save the object
    e.save()
    
    print("Data is coming")
    return redirect('/emp/home/')




