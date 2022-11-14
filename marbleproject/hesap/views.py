from django.shortcuts import render, redirect
from django.http.response import HttpResponse

# Create your views here.

def giris(request):
    return render(request, "hesap/giris.html")

def kayit(request):
    return render(request, "hesap/kayit.html")

def cikis(request):
    return redirect("giris.html")
