from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('atualiza/<id>/',views.update),
    path('delete/<id>/',views.apaga),
]