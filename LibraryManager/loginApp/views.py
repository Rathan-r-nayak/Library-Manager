from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.template import loader
from . import models
from django.contrib.auth.models import User

# Create your views here.

def welcomePage(request):
    template=loader.get_template("loginApp/index.html")
    return render(request,"loginApp/index.html")




# def signinPage(request):
#     template=loader.get_template("loginApp/signinPage.html")
#     # return HttpResponse(template.render())
#     return render(request,"loginApp/signinPage.html")

def signinInput(request):
    if request.method=='POST':
        uname=request.POST['uname']
        upasswd=request.POST['passwd']

        user=authenticate(username=uname,password=upasswd)

        if user is not None:
            login(request,user)
            messages.success(request,f"successfully logged in as {user}")
            return HttpResponseRedirect('/studentapp/')
        else:
            messages.error(request,f"failed to login")
            return redirect('main')
    
    return HttpResponse("404-Not Found")







def signupPage(request):
    template=loader.get_template("loginApp/signupPage.html")
    # return HttpResponse(template.render())
    return render(request,"loginApp/signupPage.html")

def signupInput(request):
    if request.method=='POST':
        uname=request.POST['uname']
        umail=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        cardnum=request.POST['card_num']
        upasswd=request.POST['passwd']

        ob=User.objects.create_user(username=uname,password=upasswd)
        ob.first_name=fname
        ob.last_name=lname
        ob.email=umail
        ob.save()
        
        u=models.AuthUser.objects.get(username=uname)
        user=models.User(uid=u,card_num=cardnum,total_issued=0)
        user.save()

        u=authenticate(username=uname,password=upasswd)
        login(request,u)
        return HttpResponseRedirect('/studentapp/')
    return HttpResponse("404-Not Found")












# import pandas as pd
# import numpy as np
# import csv
# def filldb(request):
#     file = open("static/database_values.csv")
#     # csvreader = csv.reader(file)
#     df=pd.read_csv(file)
#     for i in df.values:
#         bid=i[0]
#         title=i[1]
#         author=i[2]
#         year=i[3]
#         summary=i[4]
#         copies=i[5]
#         book=models.Book(book_id=bid,title=title,pub_year=year,author=author,copies=copies,summary=summary)
#         book.save()
#     return HttpResponse("added values to database")
