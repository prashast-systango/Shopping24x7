from django.shortcuts import render
from django.views import View
from .forms import AddProductsForm, AddEmployeeForm
from django.contrib import messages
from rest_framework import request
from django.http import HttpResponse

class PartnerHomeView(View):
    def get(self, request):
        return render(request, 'partner/partnerhome.html')


class AddProductsView(View):
    def get(self, request):
        fm = AddProductsForm()
        return render(request, 'partner/addproducts.html', {'form':fm})

    def post(self, request):
        fm = AddProductsForm(request.POST, request.FILES)
        if fm.is_valid():
            messages.success(request, 'Product Added Successfully !!')
            fm.save()
            # return render(request, 'partner/addproducts.html', {'form':fm})
        return render(request, 'partner/addproducts.html', {'form':fm})
        # return HttpResponse('success !!')
        

class AddEmployeeView(View):
    def get(self, request):
        fm = AddEmployeeForm()
        return render(request, 'partner/addemployee.html', {'form':fm})

    def post(self, request):
        fm = AddEmployeeForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Product Added Successfully !!')
            fm.save()
            # return render(request, 'partner/addproducts.html', {'form':fm})
        return render(request, 'partner/addemployee.html', {'form':fm})
        



# def addProductsView(request):
#     fm = AddProductsForm()
#     return render(request, 'partner/addproducts.html', {'form':fm})




# class AddProductsViewTemp(View):
#     if request.method == 'POST':
#         fm = AddProductsForm(request.POST, request.FILES)
#         if fm.is_valid():
#             messages.success(request, 'Product Added Successfully !!')
#             fm.save()





# # pylint: disable=no-self-use
# from django.shortcuts import render
# from django.views import View
# from Customer.forms import CustomerRegistrationForm
# from django.contrib import messages
# from .models import (
#     Customer,
#     Product,
#     Cart,
#     OrderPlaced,
#     Partner,
#     Coupon,
#     Employee,
#     Attendance,
#     Location
# )

# class HomeView(View):
#     def get(self, request):
#         accessories = Product.objects.filter(category='AC')
#         mobiles = Product.objects.filter(category='M')
#         laptops = Product.objects.filter(category='L')
#         return render(request, 'partner/home.html', {'accessories':accessories, 'mobiles':mobiles, 'laptops':laptops})

# # def home(request):
# #     return render(request, 'partner/home.html')

# class ProductDetailView(View):
#     def get(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         return render(request, 'partner/productdetail.html', {'product':product})


# # def product_detail(request):
# #  return render(request, 'app/productdetail.html')
# # (Oneplus,Samsung,Apple)
# class MobileView(View):
#     def get(self, request, data=None):
#         if data == None or data == 'All Mobiles':
#             mobiles = Product.objects.filter(category='M')
#         elif data == 'Oneplus' or data == 'Samsung' or data == 'Apple':
#             mobiles = Product.objects.filter(category='M').filter(brand=data)

        
#         return render(request, 'partner/mobile.html', {'mobiles':mobiles})
        
# class LaptopView(View):
#     """This class is used for filtering laptops"""
#     def get(self, request, data=None):
#         if data == None or data == 'All Laptops':
#             laptops = Product.objects.filter(category='L')
#         elif data == 'ASUS' or data == 'Lenovo' or data == 'Apple' or data=='Microsoft':
#             laptops = Product.objects.filter(category='L').filter(brand=data)

        
#         return render(request, 'partner/laptop.html', {'laptops':laptops})

# class AccessoryView(View):
#     def get(self, request, data=None):
#         if data == None or data == 'All Accessories':
#             accessories = Product.objects.filter(category='AC')      
#         return render(request, 'partner/accessories.html', {'accessories':accessories})

# class CustomerRegistrationView(View):
#     def get(self, request):
#         form = CustomerRegistrationForm()
#         return render(request, 'partner/customerregistration.html', {'form':form})
#     def post(self, request):
#         form = CustomerRegistrationForm(request.POST)
#         if form.is_valid():
#             messages.success(request, 'Regitration Successfull !!')
#             form.save()
#         return render(request, 'partner/customerregistration.html', {'form':form})



# def add_to_cart(request):
#  return render(request, 'partner/addtocart.html')

# def buy_now(request):
#  return render(request, 'partner/buynow.html')

# def profile(request):
#  return render(request, 'partner/profile.html')

# def address(request):
#  return render(request, 'partner/address.html')

# def orders(request):
#  return render(request, 'partner/orders.html')

# # def change_password(request):
# #  return render(request, 'partner/changepassword.html')


# # def login(request):
# #  return render(request, 'partner/login.html')

# # def customerregistration(request):
# #  return render(request, 'partner/customerregistration.html')

# def checkout(request):
#  return render(request, 'partner/checkout.html')
