from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate,login
# Create your views here.

def giris(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            return redirect("anasayfa")

        else:
            return render(request, "hesap/giris.html", {"error":"Kullanıcı Adı veya Parola Yanlış"})

    return render(request, "hesap/giris.html")

def kayit(request):
    return render(request, "hesap/kayit.html")

def cikis(request):
    return redirect("giris.html")
