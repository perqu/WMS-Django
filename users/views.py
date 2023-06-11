from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from WMS.decorators import group_required


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get("next")  # Odczytanie wartości atrybutu "next"
            if next_url:
                return redirect(next_url)  # Przekierowanie na poprzednią stronę
            else:
                return JsonResponse({"success": True})
        else:
            return JsonResponse(
                {"error": "Nieprawidlowa nazwa uzytkownika lub haslo."}, status=401
            )


def logout_user(request):
    logout(request)
    return redirect("home")


@group_required(["Admin", "Kieras"])
def account(request):
    return render(request, "users/account.html")
