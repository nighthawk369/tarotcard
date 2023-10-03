from django.urls import path
from tarotapp import views

urlpatterns = [
    path('glist/', views.glist),
    path('getlist/', views.list.as_view(), name='list')
    ]


