from django.shortcuts import render, redirect

from rest_framework.generics import get_object_or_404
from rest_framework.generics import (CreateAPIView, ListAPIView, 
                                     RetrieveUpdateDestroyAPIView,
                                     RetrieveUpdateDestroyAPIView)

from rest_framework import viewsets

from .models import Employee, Company, Company_Partner
from .serializers import EmployeeSerializer, CompanySerializer, Company_PartnerSerializer


class EmployeeView(ListCreateAPIView):
    """
    """

    # template_name = 'index.html'
    # context_object_name = 'employee_list'

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def perform_create(self, serializer):
        company = get_object_or_404(Company, id=self.request.data.get('company_id'))
        return 


class SingleEmployeeView(RetrieveUpdateDestroyAPIView):
    """
    To update, delete, lookup an employee.

    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CompanyView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class Company_PartnerView(ListCreateAPIView):
    queryset = Company_Partner.objects.all()
    serializer_class = Company_PartnerSerializer

    def perform_create(self, serializer):
        from_company = get_object_or_404(Company, id=self.request.data.get('company'))
        with_company = get_object_or_404(Company, id=self.request.data.get('company'))
        return serializer.save(from_company=from_company, with_company=with_company)


class SingleCompany_PartnerView(RetrieveUpadateDestroyAPIView):
    queryset = Company_Partner.objects.all()
    serializer_class = Company_PartnerSerializer


class BaseCrudMeneger():
    """ 
    Create, Edit, Delete a record.

    """

    def create(self, request):
        if request.method == 'POST':
            form = RecordForm(request.POST)

            if form.is_valid():
                form.save()
            return redirect('index')

        form = RecordForm()
        return render(request,'record.html', {'form': form})

    def edit(self, request, pk, template_name='edit.html'):
        record = get_object_or_404(Employee, pk=pk)
        form = RecordForm(request.POST or None, instance=record)

        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, template_name, {'form':form})

    def delete(self, request, pk, template_name='confirm_delete.html'):
        record = get_object_or_404(Post, pk=pk)    
        
        if request.method=='POST':
            record.delete()
            return redirect('index')

        return render(request, template_name, {'object':post})
