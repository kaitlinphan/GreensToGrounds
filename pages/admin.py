from django.contrib import admin
from .models import Product, Order

#from .models import Mission


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone_number']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

#admin.site.register(models.ProduceBox, ProductAdmin)
#admin.site.register(models.SnackBox, ProductAdmin)
#admin.site.register(models.AddOn, ProductAdmin)
#admin.site.register(Mission)
