from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Halaman Biodata Kelompok ROMUSA</h1><p>Status: Fondasi Django Berhasil!</p>")