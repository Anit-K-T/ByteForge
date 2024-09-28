from django.db import models

class Hospital(models.Model):  # Renamed to singular form
    name = models.CharField(max_length=255)  # Changed to CharField with a max_length
    resources_available = models.TextField()  # Keeping TextField if this contains detailed info

class ProductSupplier(models.Model):  # Renamed to singular form
    name = models.CharField(max_length=255)  # Changed to CharField with a max_length
    products = models.TextField()  # Assuming this is a detailed list of products
    resource_name = models.CharField(max_length=255)  # Changed to CharField with a max_length
    count = models.IntegerField()  # No change needed, correct use of IntegerField
