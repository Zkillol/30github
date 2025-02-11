from django.urls import path

from descrip_page.views import comments
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('post/<int:id>/', comments, name='comments'),  # Детальный просмотр поста
]
