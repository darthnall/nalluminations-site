from django.contrib import admin

from .models import Product, User, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "image"]

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Order)
