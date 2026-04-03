from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.utils import check_is_group_member
from .models import GlobalSetting

def index(request):
    
    tema_aktif = request.session.get('tema_css', 'tema-terang')
    font_aktif = request.session.get('font_css', 'font-sans')
    
    is_group_member = check_is_group_member(request.user)
    setting, created = GlobalSetting.objects.get_or_create(id=1)
            
    context = {
        'is_group_member': is_group_member,
        'class_tema_aktif': setting.tema,
        'class_font_aktif': setting.font,
    }
    
    return render(request, 'index.html', context)


def ubah_tampilan_tema(request):
    if request.method == 'POST':
        setting, created = GlobalSetting.objects.get_or_create(id=1)

        tema_sekarang = request.session.get('tema_css', '')
        if setting.tema == '':
                setting.tema = 'dark-theme'
        else:
            setting.tema = ''
        
        setting.save()
    return redirect('index')
    
def ubah_tampilan_font(request):
    if request.method == 'POST':
        setting, created = GlobalSetting.objects.get_or_create(id=1)

        font_sekarang = request.session.get('font_css', '')
        if setting.font == '':
                setting.font = 'serif-theme'
        else:
            setting.font = ''

        setting.save()
    return redirect('index')