'''
Classes for presentation data of models using templates.

'''

from django import forms
from .models import Employee, Company, Company_Partner


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = "__all__"


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = "__all__"


class Company_PartnerForm(forms.ModelForm):

    class Meta:
        model = Company_Partner
        fields = "__all__"