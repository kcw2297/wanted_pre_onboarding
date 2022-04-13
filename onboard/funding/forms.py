from dataclasses import field
from django.forms import ModelForm
from .models import Funding

class FundingForm(ModelForm):
    class Meta():
        model = Funding
        fields = ['title', 'image', 'description', 'limitation', 'target' ,'dday']
    
class UpdateForm(ModelForm):
    class Meta():
        model = Funding
        fields = ['title', 'image', 'description', 'limitation' ,'dday']