from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.


def employee_list(request):
    context = {'employees_list': Employee.objects.all()}
    return render(request, 'main/employee_list.html', context)


def employee_form(request):
    if request.method == "GET":
        form = EmployeeForm()
        return render(request, 'main/employee_form.html', {'form': form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list/')


def employee_update(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "GET":
        form = EmployeeForm(instance=employee)
        context = {'form': form}
        return render(request, 'main/employee_form.html', context)
    else:
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/list/')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list/')
    
