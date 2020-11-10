from django import forms
from .models import Post,Comment



class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ('title','author','category','blog_image','content','snippet')

        
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

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ('name','body')

        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
           
        }