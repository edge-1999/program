from django.urls import path

from account_management.views.login_screen import login

app_name = "account_management"

urlpatterns = [
    path('login/', login, name='HomeScreenLogin'),
]
