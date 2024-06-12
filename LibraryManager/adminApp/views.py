from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.template import loader
from . import models
from django.contrib.auth.models import User

def adminLoginPage(request):
    return render(request,"adminApp/adminLoginPage.html")

def adminSigninInput(request):
    if request.method =='POST':
        uname=request.POST['uname']
        passwd=request.POST['passwd']
        print(uname,passwd)
        user=authenticate(username=uname,password=passwd)
        if user is not None:
            if(user.is_superuser):
                print("\n",user.username,"\n")
                login(request,user)
                messages.success(request,f"successfully logged in as {user}")
                return HttpResponseRedirect('./adminDashboard/')
        else:
            # messages.info(request,'invalid user')
            messages.error(request,f"failed to login")
            return redirect("adminLoginPage")



def adminPage(request):
    return render(request,"adminApp/adminPage.html")


def bookInput(request):
    if request.method =='POST':
        pyear=request.POST['pub_year']
        # bookid=request.POST['bookid']
        title=request.POST['title']
        author=request.POST['author']
        copies=request.POST['copies']
        summary=request.POST['summary_text']
        b=models.Book(title=title,pub_year=pyear,author=author,copies=copies,summary=summary)
        b.save()
    return redirect("dashboard")
    

def adminDashboard(request):
    book=models.Book.objects.all().values()
    context={
        'books':book
    }
    template = loader.get_template('adminApp/dashboard.html')
    return HttpResponse(template.render(context,request))
    # return render(request,'adminApp/dashboard.html')


def deleteBook(request,id):
    book=models.Book.objects.get(book_id=id)
    book.delete()
    return redirect("dashboard")
