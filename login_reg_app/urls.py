from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('add_user', views.add_user),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
]