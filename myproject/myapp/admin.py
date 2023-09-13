from django.contrib import admin
from .models import PetInfo, PetHealth, Product

admin.site.register(PetInfo)
admin.site.register(PetHealth)
admin.site.register(Product)
