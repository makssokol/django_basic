from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
import datetime
from .models import Contact, ArtObject, ArtCategory

# Create your views here.

def main(request):
    title = "главная",
    
    content = {"title": title}
    return render(request, "mainapp/index.html", content)


def products(request, pk=None):
    title = "Картины"
    products = ArtObject.objects.all()[:4]
    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
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
    

    content = {"title": title, "links_menu": links_menu, "media_url": settings.MEDIA_URL}
    return render(request, "mainapp/catalog.html", content)