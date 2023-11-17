# from django.urls import path
# from . import views 

# urlpatterns = [
#     path('', views.ListaView, name='index')
# ]


# consumo_api/urls.py
from django.urls import path
from .views import ListaView, DetalleView

urlpatterns = [
    path('', ListaView.as_view(), name='lista'),
    path('<int:item_id>/', DetalleView.as_view(), name='detalle'),
]

