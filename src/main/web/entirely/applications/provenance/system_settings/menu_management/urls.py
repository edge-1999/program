from django.urls import path

from .views.home_page import home

app_name = "menu_management"

urlpatterns = [
    path('', home, name='HomePage'),
]
