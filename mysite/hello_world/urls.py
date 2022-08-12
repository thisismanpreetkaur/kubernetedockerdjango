from django.urls import path
from hello_world import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('home/', views.home_page, name='home_page'),
]