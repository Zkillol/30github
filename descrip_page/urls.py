from django.urls import path
from . import views
from .views import comments

urlpatterns = [
    path('comments/<int:id>/', views.comments, name='comments'),

    ]