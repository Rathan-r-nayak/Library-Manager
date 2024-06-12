from django.urls import include,path
from . import views

urlpatterns=[
    path("",views.homePage,name="homePage"),
    path('search',views.search,name='search'),
    path('bookDetail/<str:bookdet>',views.bookDetail,name="schemeDetails"),
    path('bookDetail/issueBook/<str:bookdet>',views.issueBook,name="issueBook"),
]