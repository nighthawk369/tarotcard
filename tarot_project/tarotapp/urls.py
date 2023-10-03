from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('api/getlist', views.list.as_view(), name='list'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('reading/',views.reading,name='reading'),
    path('astrology/',views.astrology,name='astrology'),
    path('reiki/',views.reiki,name='reiki'),
    path('contact/', views.contact, name='contact')
]
