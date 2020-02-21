from django.db import models
from django.conf import settings
from mainapp.models import ArtObject

# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="basket", on_delete=models.CASCADE)
    product = models.ForeignKey(ArtObject, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="quantity", default=0)
    add_datetime = models.DateTimeField(verbose_name="add time", auto_now_add=True)