from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import *
from datetime import date, datetime
from .form import *
from plyer import notification
import time
# Create your views here.


def home(request):
    return render(request, 'home.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("succes")
            return redirect('/')
        else:
            print("not found")
            return render(request, 'loginpage.html')
    else:
        return render(request, 'loginpage.html')


def logout(request):
    auth.logout(request)
    return redirect("/")

def viewblog(request):
    all_blogs = request.user.blog_set.order_by('?')
    return render(request, 'viewblogpage.html', {"all_blogs": all_blogs})


def deleteblog(request, pk):
    request.user.blog_set.get(id=pk).delete()
    return redirect("viewblog")

# USE DJANGO FORM

def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            CustomerProfile(
                name= form.cleaned_data['username'],
                ).save()
        return redirect('/')
    return render(request, 'registration.html',{"form":form})

def createblogpage(request):
    form = BlogForm()
    if request.method == "POST":
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author=request.user
            blog.save()
            return redirect('viewblog')
    return render(request, 'createblogpage.html',{"form":form})

def updateblog(request, pk):
    detail = request.user.blog_set.get(id=pk)
    form = BlogForm(instance=detail)
    details= {
    "form":form,
    "detail":detail
    }
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES,instance=detail)
        if form.is_valid():
            form.save()
        return redirect("viewblog")
    return render(request, 'updateblog.html', {"details":details})


def customer_profile(request):
    profile = CustomerProfile.objects.get(name=request.user)
    form = CustomerProfileForm()
    details={
    "profile":profile,
    "form":form
    }
    if request.method=="POST":
        print("fsdf")
        form= CustomerProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            print("sav")
            form.save()
        else:
            print("eror")
        return redirect("customer_profile")
    return render(request,'customer_profile.html',{"details":details})



# WITHOUT DJANGO FORMS

# def registration(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password1 = request.POST["password1"]
#         password2 = request.POST["password2"]
#         user = User.objects.create_user(
#             username=username, password=password1, email=email)
#         user.save()
#         return redirect('/')
#     return render(request, 'registration.html')


# def createblogpage(request):
#     if request.method == "POST":
#         title = request.POST["title"]
#         description = request.POST["description"]
#         new_blog = Blog(author=request.user, title=title,
#                         description=description, posted_date=date.today(),
#                         last_updated=datetime.now().strftime("%H:%M:%S"))
#         new_blog.save()
#         return redirect('viewblog')
#     return render(request, 'createblogpage.html')


# def updateblog(request, pk):
#     detail = request.user.blog_set.get(id=pk)
#     details = {
#         "detail": detail,
#     }
#     if request.method == "POST":
#         updated_title = request.POST["updated_title"]
#         updated_description = request.POST["updated_description"]
#         detail.title = updated_title
#         detail.description = updated_description
#         detail.last_updated = datetime.now().strftime("%H:%M:%S")
#         detail.save()
#         return redirect("viewblog")
#     return render(request, 'updateblog.html', {"details": details})






def notification(request):
    notification.notify(
        title="Drink Water",
        message="Drinking water after a massage is important and reduces soreness. One way to boost your odds for not being sore the next day is increase your water intake after your appointment",
        app_icon="drinkwater.ico",
        timeout=5
    )
    time.sleep(5)