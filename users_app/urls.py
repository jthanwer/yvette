from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('connexion/', views.connexion, name='login'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('profile/<int:pk>', views.detail_profile, name='detail_profile'),
]