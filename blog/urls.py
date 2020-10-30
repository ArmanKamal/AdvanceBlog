from django.urls import path,include
from .views import HomeView,ArticleDetailView,CreatePostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryList,LikeView

urlpatterns = [
    path('',HomeView.as_view(),name="list"),
    path('<int:pk>/',ArticleDetailView.as_view(),name="detail"),
    path('add_post/',CreatePostView.as_view(),name="add_post"),
    path('update/<int:pk>',UpdatePostView.as_view(),name="update"),
    path('delete/<int:pk>',DeletePostView.as_view(),name="delete"),
    path('add_category/',AddCategoryView.as_view(),name="add_category"),
    path('category/<slug:slug>',CategoryView,name="category"),
    path('category_list/',CategoryList.as_view(),name="category_list"),
    path('like/',LikeView,name="like_post"),
]
