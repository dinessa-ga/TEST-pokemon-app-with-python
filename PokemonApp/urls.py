# from django.urls import path
# from . import views 

# urlpatterns = [
#     path('', views.ListaView, name='index')
# ]


# consumo_api/urls.py
from django.urls import path
from .views import ListView, DetailsView
urlpatterns = [
    path('', ListView.as_view(), name='index'),
    path('pokemon/<int:item_id>', DetailsView.as_view(), name='pokemon'),
]

# <int:item_id>/