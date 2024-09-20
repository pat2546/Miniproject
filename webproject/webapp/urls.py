from webapp import views
from django.urls import path

urlpatterns = [
     path('', views.index),
    path('about/', views.about),
    path('form/', views.form),
    path('delete/<person_id>/', views.delete),
    path('edit/<person_id>/', views.edit),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]
