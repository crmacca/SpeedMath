from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")
    
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "users/login.html", {
                'message': {
                    "text": "Credentials combination does not match our records.",
                    "type": "Error",
                    "class": "errorBox"
                }
            })
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": {
            "text": "Successfully Logged Out",
            "type": "Success",
            "class": "successBox"
        }
    })