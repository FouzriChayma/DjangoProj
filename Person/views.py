from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import login

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("acceuil")  # fixed
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")

    context = {"register_form": form}
    return render(request, "register.html", context)

def acceuil(request):  # new view
    return render(request, "acceuil.html")



