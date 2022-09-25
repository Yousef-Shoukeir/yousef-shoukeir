from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def blog(request):
    post = Post.objects.all()
    return render(request, 'blog.html', {'post': post})
