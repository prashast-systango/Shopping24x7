# Django imports
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Local imports
from Base.models import Product
from rest_framework import request
from .models import Coupon, PartnerEmails
from Base.forms import UserRegistrationForm
from Employee.models import Employee, EmployeeEmails
from .forms import (
    AddProductsForm,
    CreateEmployeeForm,
    ProductsForm,
    EmployeesForm,
    AddCouponsForm
)


class PartnerHomeView(View):
    def get(self, request):
        return render(request, 'partner/partnerhome.html')


class ProductListView(View):
    def get(self, request):
        prod = Product.objects.all()
        return render(request, 'partner/allproductslist.html', {'item': prod})


class EmployeeListView(View):
    def get(self, request):
        emp = Employee.objects.all()
        return render(request, 'partner/allemployeeslist.html', {'item': emp})


class CouponListView(View):
    def get(self, request):
        coupon = Coupon.objects.all()
        return render(request, 'partner/allemployeeslist.html', {'item': coupon})


class AddProductsView(View):
    def get(self, request):
        fm = AddProductsForm()
        return render(request, 'partner/addproducts.html', {'form': fm})

    def post(self, request):
        fm = AddProductsForm(request.POST or None, request.FILES or None)
        print(fm)
        print(fm.data)
        if fm.is_valid():
            messages.success(request, 'Product Added Successfully !!')
            fm.save()
        return render(request, 'partner/addproducts.html', {'form': fm})


def editProductDetails(request, pk):
    prod = Product.objects.get(id=pk)
    form = ProductsForm(instance=prod)

    if request.method == 'POST':
        form = ProductsForm(request.POST, instance=prod)
        if form.is_valid():
            form.save()
            return redirect('/all_products')

    context = {'form': form}
    return render(request, 'partner/editproductdetails.html', context)


def deleteProduct(request, pk):
    prod = Product.objects.get(id=pk)
    if request.method == "POST":
        prod.delete()
        return redirect('/all_products')

    context = {'item': prod}
    return render(request, 'partner/deleteproduct.html', context)



class AddEmployeeView(View):
    def get(self, request):
        fm = UserRegistrationForm()
        return render(request, 'partner/addemployee.html', {'form': fm})

    def post(self, request):
        fm = CreateEmployeeForm(request.POST)
        email = request.POST.get('email')
        if fm.is_valid():
            messages.success(request, 'Employee Regitration Successfull !!')
            fm.save()
            EmployeeEmails.objects.create(email=email)
        return render(request, 'partner/addemployee.html', {'form': fm})

# change template name
class AddPartnerView(View):
    def get(self, request):
        fm = UserRegistrationForm()
        return render(request, 'partner/addemployee.html', {'form': fm})

    def post(self, request):
        fm = CreateEmployeeForm(request.POST)
        email = request.POST.get('email')
        if fm.is_valid():
            messages.success(request, 'Partner Regitration Successfull !!')
            fm.save()
            PartnerEmails.objects.create(email=email)
        return render(request, 'partner/addemployee.html', {'form': fm})



def editEmployeeDetails(request, pk):
    emp = Employee.objects.get(id=pk)
    form = EmployeesForm(instance=emp)

    if request.method == 'POST':
        form = EmployeesForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('/all_employees')

    context = {'form': form}
    return render(request, 'partner/editemployeedetails.html', context)


def deleteEmployee(request, pk):
    emp = Employee.objects.get(id=pk)
    if request.method == "POST":
        emp.delete()
        return redirect('/all_employees')

    context = {'item': emp}
    return render(request, 'partner/deleteemployee.html', context)


class AddCouponsView(View):
    def get(self, request):
        fm = AddCouponsForm()
        return render(request, 'partner/addcoupon.html', {'form': fm})

    def post(self, request):
        fm = AddCouponsForm(request.POST or None, request.FILES or None)
        if fm.is_valid():
            messages.success(request, 'Product Added Successfully !!')
            fm.save()
        return render(request, 'partner/addcoupon.html', {'form': fm})

# manage products using AJAX


class ManageProduct(View):
    def get(self, request):
        fm = AddProductsForm()
        prod = Product.objects.all()
        return render(request, 'partner/manageproducts.html', {'form': fm, 'item': prod})

    def post(self, request):
        fm = AddProductsForm(request.POST or None, request.FILES or None)
        prod = Product.objects.all()
        print(fm)
        print(fm.data)
        if fm.is_valid():
            messages.success(request, 'Product Added Successfully !!')
            fm.save()
        return render(request, 'partner/manageproducts.html', {'form': fm, 'item': prod})


def saveProductData(request):
    if request.method == "POST":

        form = AddProductsForm(request.POST or None, request.FILES or None)
        print(form)
        print(form.data)
        if form.is_valid():
            title = request.POST['title']
            selling_price = request.POST['selling_price']
            description = request.POST['description']
            brand = request.POST['brand']
            category = request.POST['category']
            product_image = request.POST['product_image']
            prod = Product(title=title, selling_price=selling_price, description=description,
                           brand=brand, category=category, product_image=product_image)
            prod.save()
            temp = Product.objects.values()
            product_data = list(temp)
            return JsonResponse({'status': 'Saved', 'product_data': product_data})
        else:
            return JsonResponse({'status': 0})
