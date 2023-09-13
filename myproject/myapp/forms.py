from django import forms
from .models import PetInfo, PetHealth, Product

class PetInfoForm(forms.ModelForm):
    class Meta:
        model = PetInfo
        fields = ['PetType', 'PetBreed', 'Policy', 'PolicyStartDate', 'PolicyEndDate']

class PetHealthForm(forms.ModelForm):
    class Meta:
        model = PetHealth
        fields = ['PetID', 'PetBPM', 'Latitude', 'Longitude', 'Steps']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name', 'Description', 'Price', 'ProductType', 'Stock']
