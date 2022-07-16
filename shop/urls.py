from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('error_page/', views.error_page, name='error_page'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/phones/', views.phones, name='phones'),
    path('catalog/phones/<str:name>', views.phone_id, name='phone_id'),
]
