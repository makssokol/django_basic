from django.db import models

# Create your models here.
class ArtCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    description = models.TextField(verbose_name="описание", blank=True)

    def __str__(self):
        return self.name

class ArtObject(models.Model):
    category = models.ForeignKey(ArtCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="имя объекта", max_length=128)
    image = models.ImageField(upload_to="art_images", blank=True)
    artist = models.CharField(verbose_name="автор", max_length=60, blank=True)
    description = models.TextField(verbose_name="описание объекта", blank=True)
    price = models.DecimalField(verbose_name="стоимость", max_digits=12, decimal_places=2, default=0)
    location = models.CharField(verbose_name="место", max_length=128)

    def __str__(self):
        return f"{self.name} ({self.category.name})"
