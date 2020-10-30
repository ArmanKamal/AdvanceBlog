from django.urls import path,include
from .views import UserRegisterView,login_page,UserEditProfile,PasswordChangeView,password_success
from django.contrib.auth.views import LogoutView
urlpatterns = [
 
 path('register/',UserRegisterView.as_view(),name='register'),
 path('login/', login_page, name='login'),
 path('logout/',LogoutView.as_view(),name="logout"),
 path('profile/edit',UserEditProfile.as_view(),name="edit_profile"),
 path('password/',PasswordChangeView.as_view(template_name='change-password.html')),
 path('password_success/',password_success,name="password_success")

]
