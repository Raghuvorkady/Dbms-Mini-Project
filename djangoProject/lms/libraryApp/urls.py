from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    #url(r'^emp_detail/(?P<user_name>\w+)/(?P<mobile_number>\d{10,18})/$', views.emp_detail, name='emp_detail'),
    path('addpublisherdetails/<str:option>/', views.addPublisherDetails, name="addpublisherdetail"),
    path('updatepublisherdetails/<str:pubID>/', views.updatePublisherDetails, name="updatepublisherdetail"),
    path('updateauthordetails/<str:pk>/', views.updateAuthorDetails, name="updateauthordetail"),
    path('deleteauthordetails/<str:pk>/', views.deleteAuthorDetails, name="deleteauthordetail"),
    path('deletepublisherdetails/<str:pk>/', views.deletePublisherDetails, name="deletepublisherdetail"),
    path('updatebookdetails/<str:bookID>/', views.updateBookDetails, name="updatebookdetail"),
    path('deletebookdetails/<str:bookID>/', views.deleteBookDetails, name="deletebookdetail"),
    path('addauthordetails/<str:option>/', views.addAuthorDetails, name="addauthordetail"),
    path('addbookdetails/<str:option>/', views.addBookDetails, name="addbookdetail"),
    path('addbooktemplate/', views.addBookTemplate, name="addbooktemplate"),
    path('progressive/', views.progressive),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('borrowbook/', views.borrowBook, name="borrowbook"),
    #path('/', views.borrowBook),  for staff to view all books
    path('viewbook/<str:bookID>/', views.viewBook, name="viewbook"),
    path('returnbook/', views.returnBook, name="returnbook"),
    path('manage/', views.manage, name="manage"),
    path('quicksearch/<str:book>', views.quickSearch, name="quicksearch"),
    path('signup/', views.signUp, name="signup"),
    path('signin/', views.signIn, name="signin"),
    path('search/<str:book>/', views.searchResult, name="search"),
]
