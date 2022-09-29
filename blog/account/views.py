from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



# Create your views here.
def login_(request):
    if request.user.is_authenticated:
        return redirect("index")


    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "account/login.html", {
                "error": "Username or Password is false"
            })

    return render(request, "account/login.html")

def register_(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password==repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", {
                "error":"Change username",
                "username":username,
                "email":email,
                "firstname":firstname,
                "lastname":lastname
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/register.html", {
                "error":"Email is using",
                "username":username,
                "email":email,
                "firstname":firstname,
                "lastname":lastname
                })
                else:
                    user = User.objects.create_user(username=username, email=email,
                    first_name = firstname, last_name = lastname,
                    password = password)
                    user.save()
                    return redirect("login")
        else:
            return render(request, "account/register.html", {
                "error":"Password confirmation is false",
                "username":username,
                "email":email,
                "firstname":firstname,
                "lastname":lastname
            })

    return render(request, "account/register.html")

def logout_(request):
    logout(request)
    return redirect("index")


