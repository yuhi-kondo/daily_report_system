from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Employee
from .forms import EmployeeUserForm
from django.utils.decorators import method_decorator
from django.views.generic import ListView

# Create your views here.
def home(request):
    '''トップページ'''
    return render(request, 'home.html')

""" @login_required
@staff_member_required
def employee_create(request):
    '''新規作成画面'''
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        Employee.objects.create(name=name, email=email)
        return redirect('employee_index')
    return redirect('employee_new') """

@login_required
@staff_member_required
def employee_new(request):
    if request.method == 'POST':
        form = EmployeeUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_index')
    else:
        form = EmployeeUserForm()
    return render(request, 'employees/employee_form.html', {'form':form})

""" @login_required
@staff_member_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees}) """

@method_decorator(staff_member_required, name='dispatch')
class EmployeeListView(ListView):
    model = Employee
    template_name= 'employees/index.html'
    context_object_name = 'employees'

@login_required
@staff_member_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_edit.html', {'employee':employee})

@login_required
@staff_member_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.save()
        return redirect('employee_index')
    return redirect('employee_edit', pk=pk)

@login_required
@staff_member_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_index')

@login_required
@staff_member_required
def employee_confirm_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        return redirect('employee_delete',pk=pk)
    return render(request,'employees/employee_confirm_delete.html',{"employee":employee})