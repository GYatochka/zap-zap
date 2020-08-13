from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.

class UserProfile(models.Model):
    User = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    ''' 
     stripe_costumer_id = models.CharField(
        max_length=120,
        null=True,
        blank=True
        ) 
    '''

    one_click_purchasing = models.BooleanField(
        default=False
    )

    def __str__(self):
        self.user.username


class Product(models.Model):
    product_name = models.CharField(
        verbose_name="Product Name",
        max_length=255
    )
    full_price = models.FloatField(
        null=True,
        blank=True,
        default=None
    )
    discount_price = models.FloatField(
        null=True,
        blank=True
    )
    category = models.CharField(
        null=True,
        blank=True,
        max_length=100
    )
    slug = models.SlugField(
        unique=True
    )
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        pass

    def add_to_cart(self):
        pass

    def remove_to_cart(self):
        pass


class ProductOrder(models.model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username

    def get_price(self):
        pass

    def get_discount_price(self):
        pass

    def get_total_price(self):
        pass

    def save_amount(self):
        pass


class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductOrder, through='ProductOrder')
    order_data = models.DateTimeField()
    delivered = models.BooleanField()

    def __str__(self):
        return self.user.username

    def get_total_price(self):
        pass


class Refund(models.Model):
    pass


class Payment(models.Model):
    pass


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = CountryField()
    street = models.CharField(max_length=124)
    apartment = models.CharField(max_length=130)
    zip = models.CharField(max_length=140)

    def __str__(self):
        return self.user.username

