from django.urls import path
from . import views

app_name = 'emphasoft_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
]