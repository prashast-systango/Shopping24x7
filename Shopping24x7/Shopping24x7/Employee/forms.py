from django import forms
from .models import Employee

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