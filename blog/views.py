from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,CategoryModel,Comment
from .forms import PostForm,UpdateForm,AddCommentForm
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.http import JsonResponse

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


class AddComment(CreateView):
    model = Comment
    template_name = 'blog/includes/add_comment.html'
    form_class = AddCommentForm
    
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form_class):
        form_class.instance.post_id = self.kwargs['pk']
        return super().form_valid(form_class)

class AddCategoryView(CreateView):
    model = CategoryModel
    template_name = 'blog/add_category.html'
    fields = ('title',)
    success_url = reverse_lazy('list')


def CategoryView(request,slug):
    category_list = Post.objects.filter(category__slug=slug)
    print(category_list)

    context = {
        'cat_name': slug,
        'category_list':category_list
    }

    return render(request,"blog/categories.html",context)

def LikeView(request):
    post = get_object_or_404(Post, id = request.POST.get('id'))
    user = request.user
    is_liked = False
    if user in post.likes.all():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    context = {
        "is_liked": is_liked,
        "post": post
    }
    if request.is_ajax():
        html = render_to_string('blog/includes/like_section.html',context, request=request)
        return JsonResponse({'form': html})