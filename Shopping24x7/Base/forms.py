from django.db.models import fields
# from Shopping24x7 import Customer
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _
from django.forms import widgets
from django.core.exceptions import ValidationError

class UserRegistrationForm(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email
    password1 = forms.CharField(label='Password ', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password ', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email ',required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'name':'email'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email '}
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}

