from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def giris(request):
    return HttpResponse("giriş yap sayfası")

def kayit(request):
    return HttpResponse("kayıt ol sayfası")

def cikis(request):
    return HttpResponse("çıkış yap")
