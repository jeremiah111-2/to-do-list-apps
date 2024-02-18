from django.shortcuts import render, redirect
from .models import Post
from .forms import Postform, Userregister
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
import requests


def index(request):
    posts = Post.objects.all()
    myform = Postform()
    if request.method == 'POST':
        myform = Postform(request.POST)
        if myform.is_valid:
            myform.save()
        return redirect('/')

    context = {'posts': posts, 'myform': myform}
    return render(request, 'index.html', context)

def update(request, pk):
    posts = Post.objects.get(id=pk)
    myform = Postform(instance=posts)
    if request.method == 'POST':
        myform = Postform(request.POST, instance=posts)
        if myform.is_valid:
            myform.save()
        return redirect('/')

    context = {'posts': posts, 'myform': myform}
    return render(request, 'update.html', context)

def delete(request, pk):
    posts = Post.objects.get(id=pk)

    if request.method == 'POST':
        posts.delete()
        return redirect('/')
  
    context = {'posts': posts}
    return render(request, 'delete.html', context)


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
            
        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already used')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already used')
                return redirect('register')
            else:
                 user = User.objects.create_user(email=email, username=username, password=password)
                 user.save();
                 return redirect('login')
        else:
            messages.info(request, 'password not the same')
            return redirect('register')
    else:
         return render(request, 'register.html')

    
def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credential')
            return redirect('login')


    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')
    