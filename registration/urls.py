from django.urls import path,include
from .views import UserRegisterView,login_page
from django.contrib.auth.views import LogoutView


urlpatterns = [
 
 path('register/',UserRegisterView.as_view(),name='register'),
 path('login/', login_page, name='login'),
 path('logout/',LogoutView.as_view(),name="logout")

]
