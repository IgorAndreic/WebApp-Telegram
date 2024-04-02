from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='start-page'),
    path('user-login', views.user_login, name='user-login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add-car', views.add_car, name='add-car'),
]