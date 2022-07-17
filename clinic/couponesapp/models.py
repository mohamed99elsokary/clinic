from django.db import models

# Create your models here.
class Coupon(models.Model):
    name = models.CharField(max_length=300)
    coupon = models.CharField(max_length=300)
    value = models.IntegerField()

    def __str__(self):
        return self.coupon
