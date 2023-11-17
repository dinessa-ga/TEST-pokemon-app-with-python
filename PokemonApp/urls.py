# from django.urls import path
# from . import views 

# urlpatterns = [
#     path('', views.ListaView, name='index')
# ]


# consumo_api/urls.py
from django.urls import path
from .views import ListaView, DetalleView

urlpatterns = [
    path('', ListaView.as_view(), name='index'),
    path('detalles/<int:item_id>/', DetalleView.as_view(), name='detalle_pokemon'),
]

# <int:item_id>/