from django.db.models import fields
# from Shopping24x7 import Customer
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _
from django.forms import widgets
from .models import Customer
from django.core.exceptions import ValidationError

# class CustomerRegistrationForm(UserCreationForm):
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if User.objects.filter(email=email).exists():
#             raise ValidationError("Email already exists")
#         return email
#     password1 = forms.CharField(label='Password ', widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     password2 = forms.CharField(label='Confirm Password ', widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     email = forms.CharField(label='Email ',required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'name':'email'}))
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         labels = {'email': 'Email '}
#         widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}


# class UserRegistrationForm(UserCreationForm):
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if User.objects.filter(email=email).exists():
#             raise ValidationError("Email already exists")
#         return email
#     password1 = forms.CharField(label='Password ', widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     password2 = forms.CharField(label='Confirm Password ', widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     email = forms.CharField(label='Email ',required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'name':'email'}))
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         labels = {'email': 'Email '}
#         widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}

        # model = User
        # fields = ['username', 'email', 'password1', 'password2']
        # labels = {'email': 'Email '}
        # widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}

class CustomerLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control', 'name':'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus':True, 'class':'form-control', 'name':'email'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'authcomplete':'current-password', 'class':'form-control', 'name':'password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  
        
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'autofocus':True, 'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city' ,'state' ,'zipcode']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
        'locality':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'state':forms.Select(attrs={'class':'form-control'}),
        'zipcode':forms.NumberInput(attrs={'class':'form-control'})}
     
class AddEmailToCustomerTableForm(forms.Form):
    class Meta:
        model = Customer
        fields = ['email']