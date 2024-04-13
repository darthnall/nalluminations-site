from django.db import models

class Product(models.Model):
    name = models.CharField("name", max_length=256)
    cost = models.FloatField("cost")
    price = models.FloatField("price")
    stock = models.PositiveIntegerField("stock", default=0)
    joke = models.CharField("joke", max_length=1024)
    punchline = models.CharField("punchline", max_length=256)

    def __str__(self) -> str:
        return self.name

class User(models.Model):
    first_name = models.CharField("first name", max_length=256)
    last_name = models.CharField("last name", max_length=256)
    email = models.EmailField("email address")
    phone = models.CharField("phone number", max_length=24)

    def __str__(self) -> str:
        return self.email

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user")
    products = models.ManyToManyField(Product, verbose_name="products")
    date_created = models.DateTimeField("date created", auto_now_add=True)
    date_fulfilled = models.DateTimeField("date fulfilled", null=True)

    def __str__(self) -> str:
        return self.date_created
