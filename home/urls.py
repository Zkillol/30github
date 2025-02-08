from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('post/<int:post_id>/', views.home, name='post_detail'),  # Детальный просмотр поста
]
