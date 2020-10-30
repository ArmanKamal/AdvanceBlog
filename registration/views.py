from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegisterForm,UserEditForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def password_success(request):
    return render(request, 'password_success.html',{})

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name="register.html"
    success_url = reverse_lazy('login')

class UserEditProfile(UpdateView):
    form_class = UserEditForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('list')

    def get_object(self):
        return self.request.user
    

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

