from django.shortcuts import render
from django.contrib.auth import logout
# Create your views here.
from django.shortcuts import render, redirect


from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile

from django.contrib.auth.models import User
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        ism = request.POST.get("ism")
        telefon = request.POST.get("telefon")

        if User.objects.filter(username=ism).exists():
            return render(request, "register.html", {
                "error": "Bu ism band"
            })

        user = User.objects.create_user(
            username=ism,
            password="12345678"  # vaqtincha parol
        )

        Profile.objects.create(
            user=user,
            telefon=telefon
        )

        login(request, user)   # 🔥 MUHIM

        return redirect("home")

    return render(request, "register.html")


def user_logout(request):
    logout(request)
    return redirect("home")