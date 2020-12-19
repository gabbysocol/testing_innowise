"""
Classes for admin presentation of data.
"""

from django.contrib import admin

from .models import Employee, Company, Company_Partner


class EmployeeApplicationAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'speciality', 'company')
    list_filter = ('speciality', 'company')


class Company_PartnerApplicationAdmin(admin.ModelAdmin):

    list_display = ( 'from_company', 'with_company')


admin.site.register(Company)
admin.site.register(Company_Partner, Company_PartnerApplicationAdmin)
admin.site.register(Employee, EmployeeApplicationAdmin)




