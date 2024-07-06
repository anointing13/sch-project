from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=255, unique=True)
    units_in_stock = models.IntegerField()
    price = models.FloatField()
    discount = models.FloatField(default=0.00)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    image2 = models.ImageField(null=True, blank=True, upload_to="images/")
    category = models.CharField(max_length=255)
    expiry_date = models.DateField()
    brand = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)

    def __str__(self):
        return self.name
