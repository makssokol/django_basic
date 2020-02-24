from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import datetime
from .models import Contact, ArtObject, ArtCategory
from basketapp.models import Basket
import random

# Create your views here.

def main(request):
    title = "главная",
    
    content = {"title": title}
    return render(request, "mainapp/index.html", content)

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []

def get_hot_product():
    products = ArtObject.objects.all()
    return random.sample(list(products), 1)[0]

def products(request, pk=None):
    title = "Картины"

    basket = get_basket(request.user)
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    if pk is not None:
        if pk == 0:
            products = ArtObject.objects.all().order_by("price")
            category = {"name": "all"}
        else:
            category = get_object_or_404(ArtCategory, pk=pk)
            products = ArtObject.objects.filter(category__pk=pk).order_by("price")
        content = {
            "title": title, 
            "products": products, 
            "category": category, 
            "media_url": settings.MEDIA_URL,
            "basket": basket,
            }
        return render(request, "mainapp/products_list.html", content)
    products = ArtObject.objects.all()
    content = {
        "title": title,
        "products": products,
        "media_url": settings.MEDIA_URL,
        "basket": basket,
    }
    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/products.html", content)

def contacts(request):
    title = "о нас"
    visit_date = timezone.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contacts.html", content)

def catalog(request):
    title = "Каталог"
    links_menu = ArtCategory.objects.all()
    basket = get_basket(request.user)
    hot_product = get_hot_product()
    content = {
        "title": title, 
        "links_menu": links_menu,
        "hot_product": hot_product,
        "media_url": settings.MEDIA_URL,
        "basket": basket,
        }
    return render(request, "mainapp/catalog.html", content)

def product(request, pk):
    title = "продукты"
    content = {
        "title": title,
        "product": get_object_or_404(ArtObject, pk=pk),
        "basket": get_basket(request.user),
        "media_url": settings.MEDIA_URL,
    }
    return render(request, "mainapp/product.html", content)