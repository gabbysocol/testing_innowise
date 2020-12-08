from django.db import models


# python manage.py makemigrations
# python manage.py migrate
class Company(models.Model):
    """
    """
    
    name = models.CharField(max_length=255)
    partner = models.CharField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    """

    first_name = models.CharField(max_length=120)
    last_name = models.TextField()
    spetiality = models.TextField()
    company = models.ForeignKey('Company', related_name='emploee', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.last_name