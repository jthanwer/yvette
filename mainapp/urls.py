from django.urls import path
from . import views


# app_name = 'mainapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('colocs/', views.ListColocs.as_view(), name='list_colocs'),
    # path('colocs/', views.list_colocs, name='list_colocs'),
    path('colocs/<int:pk>', views.DetailColoc.as_view(), name='detail_coloc'),
    path('colocs/delete/<int:pk>', views.DeleteColoc.as_view(), name='delete_coloc'),
    path('colocs/update/<int:pk>', views.UpdateColoc.as_view(), name='update_coloc'),
    path('colocs/<str:op>/<int:id_coloc>/', views.change_coloc, name='change_coloc'),
    path('create_coloc/', views.create_coloc, name='create_coloc')
]