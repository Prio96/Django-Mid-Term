from django.urls import path
from .views import CarDetail,BuyCar
urlpatterns = [
    path('detail/<int:id>',CarDetail.as_view(),name="CarDetail"),
    path('detail/buy/<int:id>',BuyCar,name="BuyCar"),
]