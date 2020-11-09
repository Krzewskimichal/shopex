from django.db import models


# class ProductImage(models.Model):
#     """Image of products."""
#     name = models.CharField(max_length=128, required=True, unique=True)
#     image = models.ImageField()
#     date_added = models.DateTimeField(auto_now_add=True)


class Categories(models.Model):
    """Product category."""
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Subcategories(models.Model):
    """Subcategory of categories, for example winter shoes for shoes."""
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Base model for products."""
    CHILD = 'CH'
    MALE = 'MA'
    FEMALE = 'FE'
    UNISEX = 'UN'
    GENDER_CHOICES = [
        (CHILD, 'Child'),
        (MALE, 'male'),
        (FEMALE, 'female'),
        (UNISEX, 'unisex'),
    ]
    title = models.CharField(max_length=128)
    price = models.FloatField(max_length=64)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategories, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=1024, blank=True)
    special_offer = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProductsSizes(models.Model):
    """Class connect Product with sizes and contain staff amount."""
    size = models.CharField(max_length=64)
    product = models.ManyToManyField(Product)
    amount = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.first().title} | size: {self.size} | amount: {self.amount}"
