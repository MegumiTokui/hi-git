from django.urls import path
from . import views

urlpatterns = [
    path('',views.top),
    path('first', views.first), 
    path('about', views.about),
    path('contact', views.contact),

]
