from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('colocations/', views.colocations, name='colocations'),
    path('register/', views.register, name='register'),
    path('connexion/', views.connexion, name='login'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('new_coloc/', views.create_coloc, name='new_coloc')
]