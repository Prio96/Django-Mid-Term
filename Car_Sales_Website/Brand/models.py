from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_name=models.CharField(max_length=60)
    nationality=models.CharField(max_length=60)
    
    def __str__(self):
        return self.brand_name