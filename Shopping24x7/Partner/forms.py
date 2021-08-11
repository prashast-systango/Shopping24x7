from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
# from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _
from django.forms import widgets
from constants import *
from Base.models import Product
from .models import Employee

# class CustomerRegistrationForm(UserCreationForm):
#     password1 = forms.CharField(label='Password ', widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     password2 = forms.CharField(label='Confirm Password ', widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     email = forms.CharField(label='Email ',required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         labels = {'email': 'Email '}
#         widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}

class CustomerLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'authcomplete':'current-password', 'class':'form-control'}))

# class MyPasswordChangeForm(PasswordChangeForm):
#     old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'autofocus':True, 'class':'form-control'}))
#     new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
#     new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}))

     
class AddProductsForm(forms.ModelForm):
    title = forms.CharField()
    selling_price = forms.FloatField()
    description = forms.CharField()
    brand = forms.CharField()
    category = forms.ChoiceField(choices= CATEGORY_CHOICES)
    product_image = forms.FileField()
    class Meta:
        model = Product
        fields = ['title', 'selling_price', 'description', 'brand', 'category', 'product_image']

class AddEmployeeForm(forms.ModelForm):
    employee_name = forms.CharField()
    department = forms.CharField()
    salary = forms.IntegerField()
    bank = forms.ChoiceField(choices= BANK_CHOICES)  
    bank_account = forms.IntegerField()
    class Meta:
        model = Employee
        fields = ['employee_name', 'department', 'salary', 'bank', 'bank_account']