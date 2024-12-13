from django.db import models
from django.utils.text import slugify
# Create your models here.
class BrandModel(models.Model):
    brand_name=models.CharField(max_length=60)
    nationality=models.CharField(max_length=60)
    slug=models.SlugField(max_length=100,unique=True,null=True,blank=True)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.brand_name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.brand_name