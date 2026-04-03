from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.utils import check_is_group_member

def index(request):
    
    tema_aktif = request.session.get('tema_css', 'tema-terang')
    font_aktif = request.session.get('font_css', 'font-sans')
    
    is_group_member = check_is_group_member(request.user)
            
    context = {
        'is_group_member': is_group_member,
        'class_tema_aktif': tema_aktif,
        'class_font_aktif': font_aktif,
    }
    
    return render(request, 'index.html', context)


def ubah_tampilan_tema(request):
    if request.method == 'POST':

        tema_sekarang = request.session.get('tema_css', '')
        if tema_sekarang == '':
            request.session['tema_css'] = 'dark-theme'
        else:
            request.session['tema_css'] = ''
    return redirect('index')
    
def ubah_tampilan_font(request):
    if request.method == 'POST':

        font_sekarang = request.session.get('font_css', '')
        if font_sekarang == '':
            request.session['font_css'] = 'serif-theme'
        else:
            request.session['font_css'] = ''

    return redirect('index')