from django.contrib import admin
from .models import CarModel,PurchaseModel
# Register your models here.
admin.site.register(CarModel)
admin.site.register(PurchaseModel)