from django.db import models
from main_market.models import MainMarket

# Create your models here.
class Goods(models.Model):
    goods_ID = models.CharField(max_length=300, primary_key=True)
    goods_name = models.CharField(max_length=300)
    goods_price = models.IntegerField()
    goods_stock = models.IntegerField()
    # ForeignKey (첫번째인자 외부 class, 외부 class에있는 객체가 삭제될때 연결되어있는 객체도 삭제
    # 세번째인자:역참조에 대한 이름을 정의해줌) 
    market_ID = models.ForeignKey(MainMarket, on_delete=models.CASCADE, related_name="goods")

