from django.urls import path
from . import views

urlpatterns = [
    path('', views.biodata_view, name='index'),
]