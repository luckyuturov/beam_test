from django.contrib import admin
from .models import Category, Product, Vendor

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'vendor', 'price')
    list_filter = ('category', 'vendor')
    search_fields = ('name',)
