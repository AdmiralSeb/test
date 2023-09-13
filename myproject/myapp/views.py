from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import PetInfo, PetHealth, Product
from .forms import PetInfoForm, PetHealthForm, ProductForm
from django.urls import reverse_lazy

def home(request):
    # Your home view logic here
    return render(request, 'home.html')

def add_pet(request):
    # Your add_pet view logic here
    if request.method == 'POST':
        form = PetInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet-list')  # Redirect to a page listing all pets
    else:
        form = PetInfoForm()
    
    return render(request, 'add_pet.html', {'form': form})


def add_product(request):
    # Your add_product view logic here
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')  # Redirect to a page listing all products
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form': form})

class PetInfoListView(ListView):
    model = PetInfo
    template_name = 'pet_list.html'
    context_object_name = 'pets'

class PetInfoDetailView(DetailView):
    model = PetInfo
    template_name = 'pet_detail.html'
    context_object_name = 'pet'
