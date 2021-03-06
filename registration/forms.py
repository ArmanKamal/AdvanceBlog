from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from blog.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput,max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class UserEditForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username =  forms.CharField(max_length=120,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'class':'form-control'}))
 
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio','phone_num','profile_pic','website_url','facebook_url','twitter_url','instagram_url','pinterest_url')
  