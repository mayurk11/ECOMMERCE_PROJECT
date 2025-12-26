from django.contrib import admin

from .models import category,Product,UserProfil,Order,OrderItem
# Register your models here.

admin.site.register(category)
admin.site.register(Product)
admin.site.register(UserProfil)
admin.site.register(Order)
admin.site.register(OrderItem)