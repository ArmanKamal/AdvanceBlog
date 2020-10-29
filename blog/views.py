from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,CategoryModel
from .forms import PostForm,UpdateForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = "blog/home.html"
    ordering = ['-timestamp']

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        cat_menu = CategoryModel.objects.all()
        context['cat_menu'] = cat_menu
        return context

class CategoryList(ListView):
    model = CategoryModel
    template_name = "blog/category_list.html"

  
    

class ArticleDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    
    def form_valid(self, form_class):
        form_class.instance.author = self.request.user
        return super(CreatePostView, self).form_valid(form_class)

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = UpdateForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'

    success_url = reverse_lazy('list')

class AddCategoryView(CreateView):
    model = CategoryModel
    template_name = 'blog/add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('list')


def CategoryView(request,slug):
    category_list = Post.objects.filter(category__slug=slug)
    print(category_list)

    context = {
        'cat_name': slug,
        'category_list':category_list
    }

    return render(request,"blog/categories.html",context)