from django.db import models
from Brand.models import Brand
# Create your models here.
class Car(models.Model):
    image=models.ImageField(upload_to='Car/media/uploads')
    name=models.CharField(max_length=100)
    description=models.TextField()
    quantity=models.IntegerField()
    price=models.BigIntegerField()
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='cars')
    