# python manage.py inspectdb (in stdOut)

from django.db import models


class Company(models.Model):
    
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Company_Partner(models.Model):
    """
    Class is for Many-To-Many company-company, type of partnership.

    """

    from_company = models.ForeignKey('Company', related_name='company_partner1', on_delete=models.CASCADE)
    with_company = models.ForeignKey('Company', related_name='company_partner2', on_delete=models.CASCADE)
    partnership = models.CharField(max_length=255)


class Employee(models.Model):
    """
    """

    first_name = models.CharField(max_length=120)
    last_name = models.TextField()
    speciality = models.TextField()
    company = models.ForeignKey('Company', related_name='employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.last_name