from django.urls import path
from .views import home, add_pet, add_product, PetInfoListView, PetInfoDetailView

urlpatterns = [
    path('', home, name='home'),
    path('add_pet/', add_pet, name='add-pet'),
    path('add_product/', add_product, name='add-product'),
    path('pets/', PetInfoListView.as_view(), name='pet-list'),
    path('pets/<int:pk>/', PetInfoDetailView.as_view(), name='pet-detail'),
    path('add_product/', add_product, name='add-product'),
]
