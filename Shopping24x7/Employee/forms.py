# django imports
from django import forms
from django.db.models import fields
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext, gettext_lazy as _


# local imports
from .models import(
    Employee,
    Attendance,
    AttendanceLog,
)

class EmployeeProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus':True, 'class':'form-control', 'name':'email'}))
    class Meta:
        model = Employee
        fields = ['employee_name', 'email', 'department' ,'salary' ,'bank', 'bank_account']
        widgets = {'employee_name':forms.TextInput(attrs={'class':'form-control'}),
        # 'locality':forms.TextInput(attrs={'class':'form-control'}),
        # 'city':forms.TextInput(attrs={'class':'form-control'}),
        # 'state':forms.Select(attrs={'class':'form-control'}),
        # 'zipcode':forms.NumberInput(attrs={'class':'form-control'})
        }

class EmployeePasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'autofocus':True, 'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}))

# class EmployeeAttendance(forms.ModelForm):
#     class Meta:
#         model = Attendance
        