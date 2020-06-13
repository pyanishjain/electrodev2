from django.contrib import admin
from seller.models import Category , Products,SubCategory

# Register your models here.

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(SubCategory)
