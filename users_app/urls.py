from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('connexion/', views.connexion, name='login'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('my_profile/', views.my_profile, name='my_profile'),
]