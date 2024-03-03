from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Item(models.Model):
    class Currency(models.TextChoices):
        USD = 'USD'
        EUR = 'EUR'

    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                validators=[
                                    MinValueValidator(Decimal(0.5))
                                ])

    currency = models.CharField(max_length=3,
                                choices=Currency.choices,
                                default=Currency.USD)

    def __str__(self):
        return self.name
