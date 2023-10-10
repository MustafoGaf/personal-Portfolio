from django.urls import path
from Chat import views


urlpatterns = [
    path('', views.chat, name='chat'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('setMessages/<str:room>/', views.setMessages, name='setMessages'),
    
    
]