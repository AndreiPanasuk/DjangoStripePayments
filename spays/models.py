from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stripe_price_id = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name
