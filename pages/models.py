from django.db import models
from django.utils import timezone
from datetime import date

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=19, decimal_places=2)
    orders_open = models.DateTimeField(default=timezone.now)
    orders_close = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} (${self.price})'

class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "{}:{}".format(self.product.name, self.id)

    def update_quantity(self, quantity):
        self.quantity = self.quantity + quantity
        self.save()

    def total_cost(self):
        return self.quantity * self.price

class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    
    def __str__(self):
        return "{}:{}".format(self.id, self.email)

    def total_cost(self):
        return sum([ li.cost() for li in self.lineitem_set.all() ] )

'''class SeasonLongProduct(Product):
    SEASONS = [("Sp", "Spring"), ("Fa", "Fall")]
    season = models.CharField(max_length=2, choices=SEASONS)

    def __str__(self):
        return f'{self.get_season_display()} {self.name}'

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
'''

# class AddOn(Product):
#    pass

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return "{}:{}".format(self.product.name, self.id)

    def cost(self):
        return self.price * self.quantity