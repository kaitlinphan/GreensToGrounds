from django.contrib import admin
from . import models

#from .models import Mission


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.ProduceBox, ProductAdmin)
admin.site.register(models.SnackBox, ProductAdmin)
admin.site.register(models.AddOn, ProductAdmin)
#admin.site.register(Mission)
