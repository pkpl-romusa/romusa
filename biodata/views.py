from django.shortcuts import render
from django.http import HttpResponse
from accounts.utils import check_is_group_member

def index(request):
    return HttpResponse("<h1>Halaman Biodata Kelompok ROMUSA</h1><p>Status: Fondasi Django Berhasil!</p>")

def biodata_view(request):
    # Dapatkan status otorisasi (True / False)
    is_group_member = check_is_group_member(request.user)
            
    context = {
        'is_group_member': is_group_member,
    }
    return render(request, 'biodata.html', context)