from django.test import TestCase, Client
from django.urls import reverse
from .models import PetInfo, PetHealth, Product
from .forms import PetInfoForm, PetHealthForm, ProductForm


class APITestCase(TestCase):

    def setUp(self):
        # Create test data
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to My App!")

    def test_add_pet_view(self):
        response = self.client.get(reverse('add-pet'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('add-pet'), {
            'PetType': 'DOG',
            'PetBreed': 'Golden Retriever',
            'Policy': 'Sample policy',
            'PolicyStartDate': '2023-09-15',
            'PolicyEndDate': '2024-09-15',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after a successful POST
        self.assertEqual(PetInfo.objects.count(), 1)  # Ensure data was added

    def test_add_pet_health_view(self):
        response = self.client.get(reverse('add-pet-health'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('add-pet-health'), {
            'PetID': 1,  # Replace with an existing PetInfo ID
            'PetBPM': 80,
            'Latitude': 40.7128,
            'Longitude': -74.0060,
            'Steps': 5000,
        })
        self.assertEqual(response.status_code, 302)  # Redirect after a successful POST
        self.assertEqual(PetHealth.objects.count(), 1)  # Ensure data was added

    def test_add_product_view(self):
        response = self.client.get(reverse('add-product'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('add-product'), {
            'Name': 'Dog Food',
            'Description': 'High-quality dog food',
            'Price': 19.99,
            'ProductType': 'FOOD',
            'Stock': 100,
        })
        self.assertEqual(response.status_code, 302)  # Redirect after a successful POST
        self.assertEqual(Product.objects.count(), 1)  # Ensure data was added
