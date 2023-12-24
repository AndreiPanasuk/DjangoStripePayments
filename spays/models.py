from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stripe_price_id = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name

DISCOUNT_TYPES = (
    ('Percentage', 'percent'),
    ('Fixed', 'fixed'),    
)

class Discount(models.Model):
    name = models.CharField(max_length=100, unique=True)
    dtype = models.CharField(max_length=32, choices=DISCOUNT_TYPES)
    dval = models.DecimalField(max_digits=12, decimal_places=2) 
    stripe_id = models.CharField(max_length=100)

    def __str__(self):
        if self.dtype == 'Percentage':
            return f'{self.name}: {self.dval}%'
        else:
            return f'{self.name}: ${self.dval}'


class Order(models.Model):
    odate = models.DateTimeField(auto_now_add=True)
    ouser = models.CharField(max_length=100)
    onum = models.CharField(max_length=100, blank=True)
    osum = models.DecimalField(max_digits=12, decimal_places=2) 
    items = models.ManyToManyField(Item, through='OrderItem')
    discounts = models.ManyToManyField(Discount)
    user_ip = models.CharField(max_length=32, blank=True)
    stripe_session_id = models.TextField(blank=True)
    stripe_session_url = models.TextField(blank=True)    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    oisum = models.DecimalField(max_digits=12, decimal_places=2)


