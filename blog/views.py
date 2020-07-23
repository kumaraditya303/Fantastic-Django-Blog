from django.shortcuts import render
from blog.models import Post
# Create your views here.


def index(request):
    featured_posts = Post.objects.filter(featured=True)[0:3]
    latest_posts = Post.objects.order_by('-timestamp')[0:3]
    context = {
        "featured_posts": featured_posts,
        "latest_posts": latest_posts
    }
    return render(request, "blog/index.html", context=context)
