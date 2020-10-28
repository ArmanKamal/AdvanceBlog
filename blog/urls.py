from django.urls import path,include
from .views import HomeView,ArticleDetailView,CreatePostView,UpdatePostView,DeletePostView

urlpatterns = [
    path('',HomeView.as_view(),name="list"),
    path('<int:pk>/',ArticleDetailView.as_view(),name="detail"),
    path('add_post/',CreatePostView.as_view(),name="add_post"),
    path('update/<int:pk>',UpdatePostView.as_view(),name="update"),
    path('delete/<int:pk>',DeletePostView.as_view(),name="delete")
]
