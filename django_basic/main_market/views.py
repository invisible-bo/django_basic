from django.shortcuts import render
from .models import main_market
from .forms import main_marketForm
# Create your views here.

def market_create(request):
    