from django.db import models

# Create your models here.

class EmployeeData(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=40)
    salary = models.FloatField()
    address = models.CharField(max_length=100)


    def __str__(self):
        return self.ename