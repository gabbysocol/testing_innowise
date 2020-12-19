"""
Classes for object serialization.
"""

from rest_framework import serializers

from .models import Employee, Company, Company_Partner


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name')


class Company_PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_Partner
        fields = ('id', 'from_company_id', 'with_company_id', 'partnership')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'speciality', 'company_id')
