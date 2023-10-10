from django.db import models
from django.urls import reverse
class Phone(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='shop/images')
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse("shop:detail", args=[self.id])
    