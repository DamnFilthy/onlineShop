from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('error_page/', views.error_page, name='error_page'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<str:category>/', views.gadgets, name='gadgets'),
    path('catalog/<str:category>/<str:name>', views.gadget_id, name='gadget_id'),
]
