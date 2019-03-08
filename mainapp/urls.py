from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('colocations/', views.scroll_colocs, name='colocations'),
    path('register/', views.register, name='register'),
    path('connexion/', views.connexion, name='login'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('new_coloc/', views.create_coloc, name='new_coloc')
]