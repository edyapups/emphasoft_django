from django.urls import path
from . import views

app_name = 'emphasoft_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>/', views.user_page, name='user'),
    path('edit_profile', views.edit_user, name='edit_user'),
    path('login/', views.login, name='login'),
]