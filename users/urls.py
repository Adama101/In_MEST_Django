from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user, name='users.urls'),

]
