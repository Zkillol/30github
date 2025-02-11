from django.urls import path
from . import views




urlpatterns = [
    path('', views.comments, name='comments'),  # Главная страница
    path('post/<int:post_id>/', views.comments, name='comments'),  # Детальный просмотр поста
]