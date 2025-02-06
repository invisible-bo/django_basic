from django.db import models

# Create your models here.
class MainMarket(models.Model):
    market_ID = models.CharField(max_length=300, primary_key=True)
    area = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    area_num = models.CharField(max_length=50)
    open_date = models.DateField(auto_now_add=True)
    worker_num = models.IntegerField()