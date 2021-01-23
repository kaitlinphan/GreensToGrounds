from django.db import models
from django.utils import timezone
from datetime import date

class Mission(models.Model):
    description = models.CharField(max_length=1000, default="No Description Provided")
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.description
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=19, decimal_places=2)
    orders_open = models.DateTimeField(default=timezone.now)
    orders_close = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} (${self.price})'

    class Meta:
        abstract = True

class SeasonLongProduct(Product):
    SEASONS = [("Sp", "Spring"), ("Fa", "Fall")]
    season = models.CharField(max_length=2, choices=SEASONS)

    def __str__(self):
        return f'{self.get_season_display()} {self.name}'

    class Meta:
        abstract = True

class ProduceBox(SeasonLongProduct):
    name = "Produce box"
    description = "The base package of fruits and vegetables"
    contents = models.TextField()

    class Meta:
        verbose_name_plural = "Produce boxes"


class SnackBox(SeasonLongProduct):
    name = "Snack box"
    description = "A box of snakcks"
    contents = models.TextField()

    class Meta:
        verbose_name_plural = "Snack boxes"


class AddOn(Product):
    pass
