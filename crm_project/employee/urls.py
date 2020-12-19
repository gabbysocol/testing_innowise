from django.urls import path, include, url
from rest_framework.routers import DefaultRouter

from .views import (
    EmployeeView, 
    SingleEmployeeView, 
    CompanyView, 
    Company_PartnerView, 
    SingleCompany_PartnerView, 
    BaseCrudMeneger
)


urlpatterns = [
    path('employee/', EmployeeView.as_view()),
    path('employee/<int:pk>', SingleEmployeeView.as_view()),
    path('company/', CompanyView.as_view()),
    path('company_partner/', Company_PartnerView.as_view()),
    path('company_partner/<int:pk>', SingleCompany_PartnerView.as_view()),


    

    path('eployee/', views.EmployeeView.as_view()),
    path('eployee/edit/<int:pk>/', CRUD.edit, name='edit'),
    path('eployee/add/', CRUD.add, name='add'),
    path('eployee/delete/<int:pk>/', CRUD.delete, name='delete'),

    path('company/', views.EmployeeView.as_view()),
    path('edit/<int:pk>/', CRUD.edit, name='edit'),
    path('add/', CRUD.add, name='add'),

    path('partners/', views.EmployeeView.as_view()),    
    path('partners/edit/<int:pk>/', CRUD.edit, name='edit'),
    path('partners/add/', CRUD.add, name='add'),
    path('partners/delete/<int:pk>/', CRUD.delete, name='delete'),
]