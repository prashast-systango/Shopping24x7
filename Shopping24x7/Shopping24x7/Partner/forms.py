from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.forms import widgets
from constants import *
from Base.models import Product
from .models import Employee, Coupon


class CreateEmployeeForm(UserCreationForm):
    password1 = forms.CharField(label='Password ', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password ', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email ',required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email '}
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}
     
class AddProductsForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'titleid'}))
    selling_price = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'id':'sellingpriceid'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'descriptionid'}))
    brand = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'brandid'}))
    category = forms.ChoiceField(choices= CATEGORY_CHOICES, widget=forms.Select(attrs={'class':'form-control', 'id':'categoryid'}))
    product_image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control', 'id':'productimageid', 'name':'img'}))
    class Meta:
        model = Product
        fields = ['title', 'selling_price', 'description', 'brand', 'category', 'product_image']
        


class AddCouponsForm(forms.ModelForm):
    coupon_partner = forms.CharField()
    coupon_name = forms.CharField()
    coupon_discount = forms.FloatField()
    class Meta:
        model = Coupon
        fields = ['coupon_partner', 'coupon_name', 'coupon_discount']

# this form is only for edit_product_details page
class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__' 

# this form is only for edit_employee_details page
class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' 
