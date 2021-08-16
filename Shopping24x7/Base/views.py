# django imports
from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout

# Local imorts
from Partner.models import Partner
from Customer.models import Customer
from Employee.models import Employee
from Customer.forms import CustomerLoginForm


class CommonLoginView(View):
    def get(self, request):
        # form = CustomerLoginForm()
        return render(request, 'base/login.html')
    def post(self, request):
        user_email=request.POST.get('email')
        user_password=request.POST.get('password')
        if Customer.objects.filter(email=user_email).exists():
            return HttpResponse('<h1>Customer</h1>')
        elif Employee.objects.filter(email=user_email).exists():
            return HttpResponse('<h1>Employee</h1>')
        elif Partner.objects.filter(email=user_email).exists():
            return HttpResponse('<h1>Partner</h1>')
        else:
            return HttpResponse('<h1>User does not exist</h1>')

        # user = authenticate(request, email=email, password=password)

        # if user is not None:
        #     login(request, email)
        #     redirect('home')
        # return render(request, 'base/login.html')
    