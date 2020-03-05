from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('paquetes.html', views.paquetes, name="paquetes"),
    path('index', views.index, name="index"),
    path('paquetes', views.paquetes, name="paquetes"),
    path('dashboard', views.dashboard, name="dashboard"),
]
