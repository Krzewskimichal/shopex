from django.db import models


class ProductImage(models.Model):
    """Image of products."""
    name = models.CharField(max_length=128, required=True, unique=True)
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)


class Categories(models.Model):
    """Product category."""
    name = models.CharField(max_length=128, required=True, unique=True)

    def __str__(self):
        return self.name


class Subcategories(models.Model):
    """Subcategory of categories, for example winter shoes for shoes."""
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, required=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=128, unique=True, required=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Base model for products."""
    title = models.CharField(max_length=128, required=True, unique=True)
    price = models.FloatField()
    category = models.ManyToManyField(Categories)
    description = models.CharField(max_length=1024)
    special_offer = models.BooleanField(default=False)
    quantity = models.IntegerField(max_length=64)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
