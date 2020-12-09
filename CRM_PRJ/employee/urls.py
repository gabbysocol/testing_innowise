from django.urls import path

from .views import EmployeeView, SingleEmployeeView, CompanyView, Company_PartnerView, SingleCompany_PartnerView


urlpatterns = [
    path('employee/', EmployeeView.as_view()),
    path('employee/<int:pk>', SingleEmployeeView.as_view()),
    path('company/', CompanyView.as_view()),
    path('company_partner/', Company_PartnerView.as_view()),
    path('company_partner/<int:pk>', SingleCompany_PartnerView.as_view()),
]