from django.db import models

class PetInfo(models.Model):
    PET_TYPE_CHOICES = [
        ('DOG', 'Dog'),
        ('CAT', 'Cat'),
        # Add more if needed
    ]
    PetType = models.CharField(max_length=50, choices=PET_TYPE_CHOICES)
    PetBreed = models.CharField(max_length=100)
    Policy = models.TextField()
    PolicyStartDate = models.DateField()
    PolicyEndDate = models.DateField()

class PetHealth(models.Model):
    PetID = models.ForeignKey(PetInfo, on_delete=models.CASCADE, related_name='health_records')
    TimeStamp = models.DateTimeField(auto_now_add=True)
    PetBPM = models.IntegerField()
    EarAlert = models.BooleanField()
    FoodAlert = models.BooleanField()
    DrinkAlert = models.BooleanField()
    GeoTagAlert = models.BooleanField()

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=200)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Stock = models.IntegerField()