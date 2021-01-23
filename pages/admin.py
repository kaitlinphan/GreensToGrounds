from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.ProduceBox, ProductAdmin)
admin.site.register(models.SnackBox, ProductAdmin)
admin.site.register(models.AddOn, ProductAdmin)
