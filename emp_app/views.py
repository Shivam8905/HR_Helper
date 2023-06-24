from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department

# Create your views here.


def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        dept = int(request.POST.get('dept'))
        role = int(request.POST.get('role'))
        salary = int(request.POST.get('salary'))
        bonus = int(request.POST.get('bonus'))
        phone = int(request.POST.get('phone_number'))

        new_emp = Employee(first_name=firstname, last_name=lastname, dept_id=dept, salary=salary, bonus=bonus, role_id=role,
                       phone=phone, hire_date=datetime.now())

        new_emp.save()
        return HttpResponse('Employee added Successfully')

    elif request.method == 'GET':
        return render(request, 'add_emp.html')

    else:
        return HttpResponse('Error')



def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A valid Emp ID")
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }

    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    if request.method == "POST":
        name = request.POST.get('name')
        dept = request.POST.get('department')
        role = request.POST.get('role')

        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name=dept)
        if role:
            emps = emps.filter(role__name=role)

        context = {
            'emps' : emps
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')

    else:
        return HttpResponse("Error")

def efficency_graph(request):
    first_name = Employee.objects.all().values_list('first_name', flat=True)[0:5]
    efficiency = Employee.objects.all().values_list('efficiency', flat=True)[0:5]
    
    aa = [a for a in first_name]
    bb = [b for b in efficiency]

    print(aa, bb)

    context = {
        'first_name': aa,
        'efficiency': bb
    }
    return render(request, 'efficency_graph.html', context)

