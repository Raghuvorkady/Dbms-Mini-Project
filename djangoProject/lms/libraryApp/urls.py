from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('addpublisherdetails/<str:option>/', views.addPublisherDetails, name="addpublisherdetail"),
    path('updatepublisherdetails/<str:pubID>/', views.updatePublisherDetails, name="updatepublisherdetail"),
    path('updateauthordetails/<str:pk>/', views.updateAuthorDetails, name="updateauthordetail"),
    path('deleteauthordetails/<str:pk>/', views.deleteAuthorDetails, name="deleteauthordetail"),
    path('deletepublisherdetails/<str:pk>/', views.deletePublisherDetails, name="deletepublisherdetail"),
    path('updatebookdetails/<str:bookID>/', views.updateBookDetails, name="updatebookdetail"),
    path('deletebookdetails/<str:bookID>/', views.deleteBookDetails, name="deletebookdetail"),
    path('addauthordetails/<str:option>/', views.addAuthorDetails, name="addauthordetail"),
    path('addbookdetails/<str:option>/', views.addBookDetails, name="addbookdetail"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('borrowbook/', views.borrowBook, name="borrowbook"),
    #path('/', views.borrowBook),  for staff to view all books
    path('viewbook/<str:bookID>/', views.viewBook, name="viewbook"),
    path('returnbook/', views.returnBook, name="returnbook"),
    path('manage/', views.manage, name="manage"),
    path('search/<str:book>', views.searchBook, name="search"),
    path('signup/', views.signUp, name="signup"),
    path('signin/', views.signIn, name="signin"),
    path('signout/', views.signOut, name="signout"),
    path('about/', views.about, name="about"),
    path('requestborrowbook/<int:bookid>/', views.requestBorrowBook, name="requestBorrowBook"),
    path('requestreturnbook/<int:bookid>/', views.requestReturnBook, name="requestReturnBook"),
]
