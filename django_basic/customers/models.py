from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_ID = models.CharField(max_length=300, primary_key=True)
    customer_name = models.CharField(max_length=300)
    register_date = models.DateField()
    customer_num = models.IntegerField()