from django.contrib import admin

from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'one_click_purchasing')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'full_price', 'discount_price', 'category')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'street', 'apartment')

class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_date', 'delivered')

# Register your models here
admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)