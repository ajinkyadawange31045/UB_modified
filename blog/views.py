from django.http import HttpResponse
from django.shortcuts import render, HttpResponsePermanentRedirect
from django.contrib.auth.forms import UserCreationForm
# from .forms import SignUpForm, LoginForm, PostForm
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import  authenticate,login,logout
from blog.models import Post, Category, Team, Value
from django import forms
from django.contrib.auth.models import Group


# Create your views here.
def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    # print(posts)
    cats = Category.objects.all()
    teams = Team.objects.all()
    values = Value.objects.all()
    data = {
        'posts': posts,
        'cats': cats,
        'teams':teams,
        'values':values,
    }
    return render(request, "home.html", data)

def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    # print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})

def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})



#logout
def user_logout(request):
    logout(request)
    return HttpResponsePermanentRedirect('/')

#login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request =request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password = upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully')
                    return HttpResponsePermanentRedirect('/')
        else:
            form = LoginForm()
        return render(request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/')


#signup
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Signed in successfully')
            user = form.save()
            # group = Group.objects.get(name ='Author')
            # user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})

