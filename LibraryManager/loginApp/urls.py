from django.urls import include,path
from . import views


urlpatterns=[
    path("",views.welcomePage,name="main"),
    # path("signin/",views.signinPage,name="singinPage"),
    path("signinInput",views.signinInput,name="singinInput"),


    # path("signup/",views.signupPage,name="signupPage"),
    path("signupInput",views.signupInput,name="singupInput"),
    # path("filldb/",views.filldb)
]