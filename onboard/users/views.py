from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def loginUser(request):


    if request.user.is_authenticated:
        return redirect('/')

    if request.method=='POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username is incorrect')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Password is incorrect')

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request,'User successfully logout')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('/')

    context = {'form':form, 'page':page}
    return render(request, 'users/login_register.html',context)


def userInfo(request):
    profile = request.user.profile
    fundings = profile.funding_set.all()

    context = {'fundings':fundings}
    return render(request, 'users/user_info.html',context)