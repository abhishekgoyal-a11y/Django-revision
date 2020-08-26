from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Blog
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


def registration(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        user = User.objects.create_user(
            username=username, password=password1, email=email)
        user.save()
        print("succcess")
        return redirect('/')
    return render(request, 'registration.html')


def createblogpage(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        new_blog = Blog(author=request.user, title=title,
                        description=description)
        new_blog.save()
        print("new blog created")
        return redirect('/')
    return render(request, 'createblogpage.html')


def viewblog(request):
    all_blogs = request.user.blog_set.all()
    return render(request, 'viewblogpage.html', {"all_blogs": all_blogs})


def deleteblog(request, pk):
    request.user.blog_set.get(id=pk).delete()
    return redirect("viewblog")


def updateblog(request, pk):
    detail = request.user.blog_set.get(id=pk)
    details = {
        "detail": detail,
    }
    if request.method == "POST":
        updated_title = request.POST["updated_title"]
        updated_description = request.POST["updated_description"]
        detail.title = updated_title
        detail.description = updated_description
        detail.save()
        return redirect("viewblog")
    return render(request, 'updateblog.html', {"details": details})
