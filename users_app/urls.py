from django.urls import path
from . import views

# app_name = 'users_app'
urlpatterns = [
    path('register/', views.RegisterClassView.as_view(), name='register'),
    path('connexion/', views.connexion, name='login'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('profile/<int:pk>', views.detail_profile, name='detail_profile'),
    path('update/<int:pk>', views.EditClassView.as_view(), name='update_profile'),
]