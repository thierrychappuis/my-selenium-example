import requests
from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    product_name_fr = models.CharField(max_length=500)
    brands = models.CharField(max_length=200)
    nutrition_grade_fr = models.CharField(max_length=10)
    url = models.CharField(max_length=500)
    store = models.ManyToManyField(Store)
    image_url = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.product_name_fr} {self.nutrition_grade_fr.upper()}"

    def better_products(self):
        return Product.objects.filter(
            id_category=self.id_category,
            nutrition_grade_fr__lt=self.nutrition_grade_fr
        )[:6]


class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorites",
    )
    id_compared = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Produit comparé",
        related_name="compared"
    )
    id_result = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Produit proposé",
        related_name="result"
    )

    def __str__(self):
        return self.id_compared
