from django.db import models
from django.contrib.auth.models import User
from Brand.models import BrandModel
# Create your models here.
class CarModel(models.Model):
    image=models.ImageField(upload_to='Car/media/uploads')
    name=models.CharField(max_length=100)
    description=models.TextField()
    quantity=models.IntegerField()
    price=models.BigIntegerField()
    brand=models.ForeignKey(BrandModel,on_delete=models.CASCADE,related_name='cars')
    
    def __str__(self):
        return self.name

class PurchaseModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="purchases_of_user")
    car=models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name="purchases_of_car")
    purchasing_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} - {self.car} ({self.purchasing_date})"
    
class CommentModel(models.Model):
    car=models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='comments')
    commenter=models.CharField(max_length=50)
    body=models.TextField()
    time=models.DateTimeField(auto_now_add=True)


    