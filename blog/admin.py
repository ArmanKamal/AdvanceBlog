from django.contrib import admin
from .models import Post,CategoryModel,UserProfile,Comment

admin.site.register(Post)
admin.site.register(CategoryModel)
admin.site.register(UserProfile)
admin.site.register(Comment)
# Register your models here.
