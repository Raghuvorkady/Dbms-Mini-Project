from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addpublisherdetails/', views.addPublisherDetails),
    path('addauthordetails/', views.addAuthorDetails),
    path('addbookdetails/', views.addBookDetails),
    path('addbooktemplate/', views.addBookTemplate),
    path('progressive/', views.progressive),
    path('dashboard/', views.dashboard),
    path('borrowbook/', views.borrowBook),
    #path('/', views.borrowBook),  for staff to view all books
    path('viewbook/', views.viewBook),
    path('returnbook/', views.returnBook),
    path('signup/', views.signUp),
    path('signin/', views.signIn),
]
