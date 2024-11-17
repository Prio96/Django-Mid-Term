from django.shortcuts import render,redirect
from Brand.models import BrandModel
from Car.models import CarModel
def home(request,brand_slug=None):
    car=CarModel.objects.all()
    if brand_slug is not None:
        brand=BrandModel.objects.get(slug=brand_slug)
        car=CarModel.objects.filter(brand=brand)
    brand=BrandModel.objects.all()
    return render(request,'home.html',{'cars':car,'brands':brand})


    