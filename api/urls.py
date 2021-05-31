from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('random', views.random),
    path('get_id/<int:id>', views.get_id),
]