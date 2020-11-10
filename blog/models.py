from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from ckeditor.fields import RichTextField

# Create your models here.
class CategoryModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True,unique=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    phone_num = models.CharField(max_length=120,null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank=True,upload_to="images/profile")
    website_url = models.CharField(max_length=255,null=True,blank=True)
    facebook_url = models.CharField(max_length=255,null=True,blank=True)
    twitter_url = models.CharField(max_length=255,null=True,blank=True)
    instagram_url = models.CharField(max_length=255,null=True,blank=True)
    pinterest_url = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=255)
    blog_image = models.ImageField(null=True,blank=True, upload_to="images/")
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    content = RichTextField(blank=True,null=True)
    snippet = models.CharField(max_length=255)
    featured = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(CategoryModel,on_delete=models.SET_NULL,null=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return self.title + ' | '+ str(self.author)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    
def pre_save_cat_slug_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    

pre_save.connect(pre_save_cat_slug_receiver,sender=CategoryModel)
    

