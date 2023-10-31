from django.contrib import admin
from .models import Post

# Register your models here.

# admin.site.register(Post)

# control how the fields will be displayed inside the database

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "post_date")

admin.site.register(Post, PostAdmin)