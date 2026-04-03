from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ubah-tampilan/', views.ubah_tampilan, name='ubah_tampilan'),
]