from django.db import models

# Create your models here.
class Employees(models.Model):
    EmployeeId = models.CharField(max_length=10, primary_key=True)
    EmployeeName = models.CharField(max_length=100, default = "")
    DateOfBirth = models.DateField(default="1950-01-01")
    DateOfJoining = models.DateField(default="1950-01-01")
    MobileNo = models.CharField(max_length=12, default = "")
    EmailId = models.EmailField(default = "")
    Department = models.CharField(max_length=100, default = "")
    Designation = models.CharField(max_length=50, default = "")
    Location = models.CharField(max_length=50, default = "")
