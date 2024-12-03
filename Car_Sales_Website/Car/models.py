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
    buyers=models.ManyToManyField(User,related_name='purchased_cars',blank=True)
class CommentModel(models.Model):
    car=models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='comments')
    commenter=models.CharField(max_length=50)
    body=models.TextField()
    time=models.DateTimeField(auto_now_add=True)


    