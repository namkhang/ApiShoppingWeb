from django.urls import path
from . import views


urlpatterns = [
    path('store_owner/' , views.store_owner),
    path('store_owner_detail/<str:id>' , views.store_owner_detail),
    path('store/' , views.store),
    path('store_detail/<str:id>' , views.store_detail),
]
