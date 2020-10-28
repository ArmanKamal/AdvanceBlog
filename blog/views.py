from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm,UpdateForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = "blog/home.html"
    ordering = ['-timestamp']

class ArticleDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = UpdateForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'

    success_url = reverse_lazy('list')
