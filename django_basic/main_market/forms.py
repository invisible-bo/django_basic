from django import forms
from .models import main_market

class main_marketForm(forms.ModelForm):
    class Meta:
        model = main_market
        fields = [
            'market_ID', 
            'area', 
            'name', 
            'area_num', 
            'worker_num',
        ]
