from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from authapp.forms import ArtShopUserLoginForm, ArtShopUserRegisterForm, ArtShopUserEditForm

# Create your views here.

def login(request):
    title = "вход"

    login_form = ArtShopUserLoginForm(data=request.POST or None)
    if request.method == "POST" and login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("main"))
    
    content = {"title": title, "login_form": login_form}
    return render(request, "authapp/login.html", content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main"))

def register(request):
    title = "регистрация"

    if request.method == "POST":
        register_form = ArtShopUserRegisterForm(request.Post, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse("auth:login"))
    
    else:
        register_form = ArtShopUserRegisterForm()

    content = {"title": title, "register_form": register_form}
    return render(request, "authapp/register.html", content)

def edit(request):
    title = "редактирование"

    if request.method == "POST":
        edit_form = ArtShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("auth:edit"))
    else:
        edit_form = ArtShopUserEditForm(instance=request.user)
    content = {"title": title, "edit_form": edit_form, "media_url": settings.MEDIA_URL}
    return render(request, "authapp/edit.html", content)
