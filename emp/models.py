from django.db import models

# Create your models here.
class emp(models.Model):
    name = models.CharField(max_length=200, default="Not Provided")
    emp_id = models.CharField(max_length=200, default="Not Provided")
    phone = models.CharField(max_length=10, default="Not Provided")
    address = models.CharField(max_length=200, default="Not Provided")  # Added default value
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=200, default="Not Provided")
