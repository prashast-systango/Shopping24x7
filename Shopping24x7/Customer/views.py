from Customer.models import Customer
from os import name, stat
from django.shortcuts import render, HttpResponse
from django.views import View
from Customer.forms import CustomerRegistrationForm, CustomerProfileForm, AddEmailToCustomerTableForm
from django.contrib import messages
from Base.models import Product
from Customer.models import CustomerEmails

class HomeView(View):
    def get(self, request):
        accessories = Product.objects.filter(category='AC')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        return render(request, 'customer/home.html', {'accessories':accessories, 'mobiles':mobiles, 'laptops':laptops})



class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'customer/productdetail.html', {'product':product})

class MobileView(View):
    def get(self, request, data=None):
        if data == None or data == 'All Mobiles':
            mobiles = Product.objects.filter(category='M')
        elif data == 'Oneplus' or data == 'Samsung' or data == 'Apple':
            mobiles = Product.objects.filter(category='M').filter(brand=data)

        
        return render(request, 'customer/mobile.html', {'mobiles':mobiles})
        
class LaptopView(View):
    """This class is used for filtering laptops"""
    def get(self, request, data=None):
        if data == None or data == 'All Laptops':
            laptops = Product.objects.filter(category='L')
        elif data == 'ASUS' or data == 'Lenovo' or data == 'Apple' or data=='Microsoft':
            laptops = Product.objects.filter(category='L').filter(brand=data)

        
        return render(request, 'customer/laptop.html', {'laptops':laptops})

class AccessoryView(View):
    def get(self, request, data=None):
        if data == None or data == 'All Accessories':
            accessories = Product.objects.filter(category='AC')      
        return render(request, 'customer/accessories.html', {'accessories':accessories})

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'customer/customerregistration.html', {'form':form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        email = request.POST.get('email')
        # add_email = AddEmailToCustomerTableForm(email=email)
        if form.is_valid():
            messages.success(request, 'Regitration Successfull !!')
            form.save()
            customer_email = CustomerEmails.objects.create(email=email)
            # customer_email.save()
        return render(request, 'customer/customerregistration.html', {'form':form})

class profileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'customer/profile.html', {'form':form, 'active':'btn-danger text-dark'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations !! Profile Updated Successfully')
            form.save()
        return render(request, 'customer/profile.html', {'form':form, 'active':'btn-danger text-dark'})





def add_to_cart(request):
 return render(request, 'customer/addtocart.html')

def buy_now(request):
 return render(request, 'customer/buynow.html')



def address(request):
 return render(request, 'customer/address.html')

def orders(request):
 return render(request, 'customer/orders.html')

def checkout(request):
 return render(request, 'customer/checkout.html')
