from django.shortcuts import render

from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Employee, Company, Company_Partner
from .serializers import EmployeeSerializer, CompanySerializer, Company_PartnerSerializer


class EmployeeView(ListCreateAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def employee_create(self, serializer):
        company = get_object_or_404(Company, id=self.request.data.get('company_id'))
        return serializer.save(company=company)


class SingleEmployeeView(RetrieveUpadateDestroyAPIView):
    """
    To update, delete, lookup 1 an employee.

    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CompanyView(ListCreateAPIView):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class Company_PartnerView(ListCreateAPIView):

    queryset = Company_Partner.objects.all()
    serializer_class = Company_PartnerSerializer

    def company_partner_create(self, serializer):
        from_company = get_object_or_404(Company, id=self.request.data.get('company'))
        with_company = get_object_or_404(Company, id=self.request.data.get('company'))
        return serializer.save(from_company=from_company, with_company=with_company)


class SingleCompany_PartnerView(RetrieveUpadateDestroyAPIView):

    queryset = Company_Partner.objects.all()
    serializer_class = Company_PartnerSerializer
