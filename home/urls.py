from django.urls import path

from descrip_page.views import comments
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Keep it as a homepage without ID
]
