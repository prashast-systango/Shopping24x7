# django imports
from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login

# Local imorts
from Partner.models import Partner, PartnerEmails
from Customer.models import Customer, CustomerEmails
from Employee.models import Employee, EmployeeEmails
from Customer.forms import CustomerLoginForm


class CommonLoginView(LoginView):
    def get(self, request):
        form = CustomerLoginForm()
        return render(request, 'base/login.html', {'form':form})
    def post(self, request):
        user_name = request.POST.get('username')
        user_email=request.POST.get('email')
        user_password=request.POST.get('password')
        print(user_email+" "+user_name+" "+user_password)
        user = authenticate(username=user_name, password=user_password)
        print(user)
        if user is not None:
            if CustomerEmails.objects.filter(email=user_email).exists():
                login(request, user)
                return render(request, 'customer/home.html')
            elif EmployeeEmails.objects.filter(email=user_email).exists():
                login(request, user)
                return render(request, 'employee/employeehome.html')
                
            elif PartnerEmails.objects.filter(email=user_email).exists():
                login(request, user)
                return render(request, 'partner/partnerhome.html')
            else:
                return HttpResponse('<h1>User does not exist</h1>')

        else:
            return HttpResponse('<h1>email and password were incorrect !!</h1>')

        # user = authenticate(request, email=email, password=password)

        # if user is not None:
        #     login(request, email)
        #     redirect('home')
        # return render(request, 'base/login.html')
    