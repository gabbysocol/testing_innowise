from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Employee
from .serializers import ArticleSerializer


class ArticleView(APIView):
    
    def get(self, request):
        """
        """"

        employee = Employee.objects.all()
        serializer = EmployeeSerializer(articles, many=True)
        return Response({"employee": serializer.data})


    def post(self, request):
        """
        """

        employee = request.data.get('employee')        
        serializer = EmployeeSerializer(data=employee)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' added successfully".format(employee_saved.first_name + employee_saved.last_name)})

    
    def delete(self, request, pk):
    
        employee = get_object_or_404(Employee.objects.all(), pk=pk)
        employee.delete()
        return Response({
            "message": "Employee with id `{}` has been deleted.".format(pk)
        }, status=204)


    def put(self, request, pk):
        saved_employee = get_object_or_404(Employee.objects.all(), pk=pk)
        data = request.data.get('employee')
        serializer = EmployeeSerializer(instance=saved_employee, data=data, partial=True)   # partial for part update
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({
            "success": "Employee '{}' updated successfully".format(employee_saved.first_name + employee_saved.last_name)
        })