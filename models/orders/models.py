from django.db import models
from accounts import views
import datetime

# Create your models here.
class Order(models.Model):
    timestamp = models.DateTimeField(blank=True)
    item = models.ForeignKey('paintings.Painting', on_delete=models.CASCADE)
    buyer = models.ForeignKey(
        'accounts.Buyer', on_delete=models.CASCADE)
    seller = models.ForeignKey(
        'accounts.Seller', on_delete=models.CASCADE)

    def __str__(self):
        return self.item
