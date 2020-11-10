from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegisterForm,UserEditForm,CreateProfileForm
from blog.models import UserProfile
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def password_success(request):
    return render(request, 'password_success.html',{})

def user_profile(request):
    return render(request, 'user_profile.html')


class CreateProfilePage(CreateView):
    model = UserProfile
    template_name = "create_profile.html"
    form_class = CreateProfileForm
    success_url = reverse_lazy('list')
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




class ShowProfile(DetailView):
    model = UserProfile
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       # users = UserProfile.objects.all()
        page_user = get_object_or_404(UserProfile, id=self.kwargs.get('pk'))
        context["page_user"] = page_user
        return context
    

class EditProfilePageView(UpdateView):
    model = UserProfile
  
    template_name = 'edit_profile_page.html'
  
    fields =['bio','phone_num','profile_pic','website_url','facebook_url','twitter_url','instagram_url','pinterest_url']
    
    success_url = reverse_lazy('list')



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

