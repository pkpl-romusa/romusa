from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ubah-tampilan-tema/', views.ubah_tampilan_tema, name='ubah_tampilan_tema'),
    path('ubah-tampilan-font/', views.ubah_tampilan_font, name='ubah_tampilan_font'),
]