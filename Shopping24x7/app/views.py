from django.shortcuts import render
from django.views import View
from .forms import CustomerRegistrationForm
from django.contrib import messages
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced,
    Partner,
    Coupon,
    Employee,
    Attendance,
    Location
)

class HomeView(View):
    def get(self, request):
        accessories = Product.objects.filter(category='AC')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        return render(request, 'app/home.html', {'accessories':accessories, 'mobiles':mobiles, 'laptops':laptops})

# def home(request):
#     return render(request, 'app/home.html')

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product':product})


# def product_detail(request):
#  return render(request, 'app/productdetail.html')
# (Oneplus,Samsung,Apple)
class MobileView(View):
    def get(self, request, data=None):
        if data == None or data == 'All Mobiles':
            mobiles = Product.objects.filter(category='M')
        elif data == 'Oneplus' or data == 'Samsung' or data == 'Apple':
            mobiles = Product.objects.filter(category='M').filter(brand=data)

        
        return render(request, 'app/mobile.html', {'mobiles':mobiles})
        
class LaptopView(View):
    def get(self, request, data=None):
        if data == None or data == 'All Laptops':
            laptops = Product.objects.filter(category='L')
        elif data == 'ASUS' or data == 'Lenovo' or data == 'Apple' or data=='Microsoft':
            laptops = Product.objects.filter(category='L').filter(brand=data)

        
        return render(request, 'app/laptop.html', {'laptops':laptops})

class AccessoryView(View):
    def get(self, request, data=None):
        if data == None or data == 'All Accessories':
            accessories = Product.objects.filter(category='AC')      
        return render(request, 'app/accessories.html', {'accessories':accessories})

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Regitration Successfull !!')
            form.save()
        return render(request, 'app/customerregistration.html', {'form':form})



def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')


# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
