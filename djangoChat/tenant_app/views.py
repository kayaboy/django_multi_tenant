from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register_tenant(request):
    form = UserCreationForm()
    u = User.objects.all()
    print(u)
    # djangodrivesmenuts
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/auth/register/")
    return render(request, "tenant_app/register.html", {"form": form})

