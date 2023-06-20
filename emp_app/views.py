from datetime import datetime

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



def remove_emp(request):
    return render(request, 'remove_emp.html')


def filter_emp(request):
    return render(request, 'filter_emp.html')

