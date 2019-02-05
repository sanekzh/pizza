from django.contrib import admin
from pizza.apps.pizza.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'id']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name', 'price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
