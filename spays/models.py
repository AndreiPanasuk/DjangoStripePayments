from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stripe_price_id = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    odate = models.DateTimeField(auto_now_add=True)
    ouser = models.CharField(max_length=100)
    onum = models.CharField(max_length=100, blank=True)
    osum = models.DecimalField(max_digits=12, decimal_places=2) 
    items = models.ManyToManyField(Item, through='OrderItem')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    oisum = models.DecimalField(max_digits=12, decimal_places=2)
