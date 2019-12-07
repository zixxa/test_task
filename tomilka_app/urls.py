from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('whysotasty', views.whysotasty, name='list-1'),
    path('health', views.health, name='list-2'),
    path('types', views.types, name='list-3'),
    path('qar', views.qar, name='list-4'),
]
