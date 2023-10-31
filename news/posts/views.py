from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post

# Create your views here.

def posts(request):
    allposts = Post.objects.all().values()
    template = loader.get_template('all_posts.html')
    context = {
        'allposts': allposts,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    post = Post.objects.get(id=id)
    template = loader.get_template('single_post.html')
    context = {
        'post': post
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())