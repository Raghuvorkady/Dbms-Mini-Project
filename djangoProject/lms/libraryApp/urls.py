from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('test/', views.test),
    path('test2/', views.test2),
    path('test3/', views.test3),
    path('test4/', views.test4),
    path('progressive/', views.progressive),
    path('dashboard/', views.dashboard),
    path('borrowbook/', views.borrowBook),
    path('viewbook/', views.viewBook),
    path('returnbook/', views.returnBook),
    path('signup/', views.signUp),
    path('signin/', views.signIn),
]
