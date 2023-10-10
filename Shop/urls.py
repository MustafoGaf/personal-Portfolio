
from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('', views.shop),
    path("<int:shop_id>/", views.detail, name='detail')
 
]