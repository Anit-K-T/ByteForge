from django.contrib import admin
from .models import Hospital, ProductSupplier  # Import your models

# Register your models
admin.site.register(Hospital)
admin.site.register(ProductSupplier)
