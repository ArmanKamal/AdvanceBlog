from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from .forms import LoginForm


# Create your views here.

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name="register.html"
    success_url = reverse_lazy('login')
    

def login_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(user.is_authenticated)
            return redirect("list")
        # A backend authenticated the credentials
        else:
            print("Failed")
    return render(request,"login.html",context={"form": form})