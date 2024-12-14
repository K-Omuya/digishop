from django.core.files.uploadedfile import UploadedFile
from django.db import models
from django.contrib.auth.models import User



# MEMBER REGISTRATION

class Members(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username



class Platform(models.Model):
    """Model to store e-commerce platforms."""
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name

class Product(models.Model):
    """Model to store product details."""
    name = models.CharField(max_length=255)
    description = models.TextField()
    platforms = models.ManyToManyField(Platform, through='ProductPrice')

    def __str__(self):
        return self.name

class ProductPrice(models.Model):
    """Model to store price details for each product on different platforms."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.platform.name}: {self.price}"



# UploadedFile
# models.py

from django.db import models

class Item(models.Model):  # Renamed from Product to Item
    name = models.CharField(max_length=255)
    description = models.TextField()
    # other fields

    def __str__(self):
        return self.name

class ItemPrice(models.Model):  # Renamed from ProductPrice to ItemPrice
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # Updated reference to Item
    price = models.DecimalField(max_digits=10, decimal_places=2)
    platform = models.CharField(max_length=255)
    # other fields as needed

    def __str__(self):
        return f"{self.item.name} - {self.price} on {self.platform}"




class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.fullname