from django.contrib import admin

from dmezapp.models import Product,Today,Best,Covid, newregis, Customer, Order, OrderItem, ShippingAddress
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Today)
dmin.site.register(Covid)
admin.site.register(Best)
admin.site.register(newregis)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
