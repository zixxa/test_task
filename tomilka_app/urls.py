from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='name'),
    path('index.html', views.index, name='name'),
    path('link-1.html', views.whysotasty, name='whysotasty'),
    path('link-2.html', views.health, name='health'),
    path('link-3.html', views.types, name='types'),
    path('link-4.html', views.qar, name='qar'),
]
