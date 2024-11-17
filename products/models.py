from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=150)
    categories = models.ManyToManyField(Category, related_name="vendors")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, blank=True, null=True, related_name="products")

    def __str__(self):
        return self.name
