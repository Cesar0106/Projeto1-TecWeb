from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<id>/',views.update, name = "update"),
    path('delete/<id>/',views.delete, name = "delete"),
]