from django.contrib import admin
from mainapp.models import ProductCategory, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')


admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
