from django.db import models

# Create your models here.


class Product(models.Model):

    name = models.CharField("Product name", max_length = 60)
    price = models.PositiveIntegerField("Product price")
    description = models.TextField("Product description")
    image = models.ImageField("Product image", upload_to='images/')

    def __str__(self) -> str:
        return self.name