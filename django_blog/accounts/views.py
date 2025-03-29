from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

# Register View
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("profile")  
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect("login")

# Profile View
def profile_view(request):
    return render(request, "accounts/profile.html", {"user": request.user})


from django.contrib.auth.decorators import login_required

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, "accounts/edit_profile.html", {"form": form})
