from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.template import loader
from . import models
import pickle
from datetime import timedelta
from datetime import date
import random
from django.contrib.auth.models import User
from joblib import load
books = load('./static/new.joblib')
similarity = load('./static/sim.joblib')

# Create your views here.
def homePage(request):
    li=[]
    for i in range(16):
        a=random.randint(1,15000)
        li.append(models.Book.objects.get(book_id=a))
    context={
        'books':li,
    }
    template=loader.get_template("studentApp/homePage.html")
    return HttpResponse(template.render(context,request))
    # return render(request,"studentApp/homePage.html")



def search(request):
    search_query=request.GET['searchQuery']
    if(search_query==""):
        return redirect("homePage")
    if len(search_query)>80:
        allbooks=models.Schemes.objects.none()
    else:
        alltitle=models.Book.objects.filter(title__icontains=search_query)
        allauthor=models.Book.objects.filter(author__icontains=search_query)
        allsummary=models.Book.objects.filter(summary__icontains=search_query)
        allbooks=alltitle.union(allauthor,allsummary)



    context={'book':allbooks,
         'query':search_query,
        }
    return render(request,'studentApp/search.html',context)



def bookDetail(request,bookdet):
    bookOb=models.Book.objects.get(title=bookdet)
    # books= pickle.load(open('book_rec.pkl','rb'))
    # similarity = pickle.load(open('similarity.pkl','rb'))
    rec_book=recommendation(bookOb.title,books,similarity)
    print("\n\n\n\n")
    print("-----------------------------------------------")
    li=[]
    for i in rec_book:
        try:
            print(i)
            li.append(models.Book.objects.get(title=i))
        except:
            continue
    print("-----------------------------------------------")
    # print(request.user)
    print("\n\n\n\n")
    # try:
    #     benftOb=models.Benifits.objects.filter(stitle=schmOb).values()
        
    # except:
    #     benftOb=None
    context={
        'book':bookOb,
        'rec_books':li
    }
    template = loader.get_template('studentApp/bookDetail.html')
    return HttpResponse(template.render(context,request))


def recommendation(b_title,books,similarity):
    index = books[books['title'] == b_title].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_book_names = []
    for i in distances[1:22]:
        # fetch the movie poster
        movie_id = books.iloc[i[0]].book_id
        recommended_book_names.append(books.iloc[i[0]].title)
    return recommended_book_names


def issueBook(request,bookdet):
    bookOb=models.Book.objects.get(title=bookdet)
    user=request.user
    print("------------------\n")
    print(user)
    print("\n------------------\n")
    userob=models.AuthUser.objects.get(username=user)

    date_out = date.today()
    print("Today's date:", date_out)
    due_date=date_out+timedelta(days=15)
    lOb=models.Lending(book=bookOb,uid=userob,date_out=date_out,due_date=due_date)
    lOb.save()
    lendingOb=models.Lending.objects.get(book=bookOb,uid=userob)
    auth=models.AuthUser.objects.get(username=user)
    context={
        'books':bookOb,
        'user':userob,
        'lending':lendingOb,
        'auth':auth,
        'uname':user

    }
    template=loader.get_template("studentApp/ack.html")
    return HttpResponse(template.render(context,request))
    # return render(request,"studentApp/ack.html")