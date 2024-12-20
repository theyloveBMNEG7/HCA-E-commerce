from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    comment = models.TextField(blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"
