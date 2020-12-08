from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('addpublisherdetails/', views.addPublisherDetails, name="addpublisherdetail"),
    path('addauthordetails/', views.addAuthorDetails, name="addauthordetail"),
    path('addbookdetails/', views.addBookDetails, name="addbookdetail"),
    path('addbooktemplate/', views.addBookTemplate, name="addbooktemplate"),
    path('progressive/', views.progressive),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('borrowbook/', views.borrowBook, name="borrowbook"),
    #path('/', views.borrowBook),  for staff to view all books
    path('viewbook/<str:bookID>/', views.viewBook, name="viewbook"),
    path('returnbook/', views.returnBook, name="returnbook"),
    path('signup/', views.signUp, name="signup"),
    path('signin/', views.signIn, name="signin"),
    path('search/<str:book>/', views.searchResult, name="search"),
]
