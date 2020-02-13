from django.shortcuts import render
import datetime

# Create your views here.

def main(request):
    title = "главная",
    
    content = {"title": title}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = "Картины"
    products = [
        {
            "name": "Сикстинская мадонна",
            "desc": "Вершина Возрождения",
            "author": "Рафаэль Санти",
            "image_src": "sixt_madonna.jpg",
            "image_href": "/products/1/",
            "alt": "картина 1",
        },
        {
            "name": "Ночной дозор",
            "desc": "Фламандский шедевр",
            "author": "Рембрандт",
            "image_src": "nightwatch.jpg",
            "image_href": "/products/2/",
            "alt": "картина 2",
        }
    ]
    content = {"title": title, "products": products}
    return render(request, "mainapp/products.html", content)

def contacts(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    content = {"title": title, "visit_date": visit_date}
    return render(request, "mainapp/contacts.html", content)

def catalog(request):
    title = "Каталог"
    links_menu = [
        {'href': 'catalog_renessaince', 'name': 'Ренессанс'},
        {'href': 'catalog_flemisch', 'name': 'Фламандцы'},
        {'href': 'catalog_impressionism', 'name': 'Импрессионизм'},
        {'href': 'catalog_russian', 'name': 'Русское искусство'},
        {'href': 'catalog_avanguard', 'name': 'Авангард'},
    ]
    content = {"title": title, "links_menu": links_menu}
    return render(request, "mainapp/catalog.html", content)