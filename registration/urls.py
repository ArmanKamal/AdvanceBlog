from django.urls import path,include
from .views import UserRegisterView,login_page,UserEditProfile,PasswordChangeView,password_success,user_profile,ShowProfile,EditProfilePageView,CreateProfilePage
from django.contrib.auth.views import LogoutView
urlpatterns = [
 
 path('register/',UserRegisterView.as_view(),name='register'),
 path('login/', login_page, name='login'),
 path('logout/',LogoutView.as_view(),name="logout"),
 path('profile/edit',UserEditProfile.as_view(),name="settings"),
 path('password/',PasswordChangeView.as_view(template_name='change-password.html')),
 path('password_success/',password_success,name="password_success"),
 path('<int:pk>/profile/',ShowProfile.as_view(), name="user_profile"),
 path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(), name="edit_profile_page"),
 path('create_profile_page/',CreateProfilePage.as_view(), name="create_profile_page")


]
