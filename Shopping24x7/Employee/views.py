# django imports
from django.views import View
from django.shortcuts import render
from django.contrib import messages

#  local imports
from .forms import EmployeeProfileForm, Employee


class EmployeeHomeView(View):
    def get(self, request):
        return render(request, 'employee/employeehome.html')

# Create your views here.
class EmployeeProfileView(View):
    def get(self, request):
        form = EmployeeProfileForm()
        return render(request, 'employee/profile.html', {'form': form, 'active': 'btn-danger text-dark'})

    def post(self, request):
        form = EmployeeProfileForm(request.POST)
        if form.is_valid():
            bank_account = form.cleaned_data['bank_account']
            employee_name = form.cleaned_data['employee_name']
            email = form.cleaned_data['email']
            department = form.cleaned_data['department']
            salary = form.cleaned_data['salary']
            bank = form.cleaned_data['bank']
            reg = Employee(bank_account=bank_account, employee_name=employee_name, email=email,
                           department=department, salary=salary, bank=bank)
            reg.save()
            messages.success(
                request, 'Congratulations !! Profile Updated Successfully')
            form.save()
        return render(request, 'employee/profile.html', {'form': form, 'active': 'btn-danger text-dark'})

