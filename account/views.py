from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from . forms import LoginForm, RegistrationForm

# Create your views here.

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])

            if user:
                login(request, user)
                return HttpResponse("Welcome You. You have been authenticated successfully")
            else:
                return HttpResponse("Sorry. Your username or password is not right.")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})

def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False) #还没有保存到数据库
            new_user.set_password(user_form.cleaned_data['password']) #设置密码
            new_user.save() #保存到数据库
            return HttpResponse("successfully")
        else:
            return HttpResponse("Sorry, you can not register.")
    else:
        user_form = RegistrationForm()
        return render(request, "account/register.html", {"form": user_form})


