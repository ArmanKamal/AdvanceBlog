from django import forms
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ('title','author','category','content','snippet')

        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','type':'hidden'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'})
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ('title','content')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'})
             }