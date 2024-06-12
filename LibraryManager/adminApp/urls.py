from django.urls import include,path
from . import views


urlpatterns=[
    path("",views.adminLoginPage,name="adminLoginPage"),
    path("adminSigninInput",views.adminSigninInput),
    path("adminDashboard/",views.adminDashboard,name="dashboard"),
    path("adminDashboard/deletedata/<int:id>",views.deleteBook,name="deleteBook"),
    
    path("adminDashboard/adminPage/",views.adminPage,name="adminPage"),
    path("adminDashboard/adminPage/bookInput",views.bookInput),
]