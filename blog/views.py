# Create your views here.
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, render

from blog.models import Post


def index(request):
    featured_posts = Post.objects.filter(featured=True)[0:3]
    latest_posts = Post.objects.order_by('-timestamp')[0:3]
    context = {
        "featured_posts": featured_posts,
        "latest_posts": latest_posts
    }
    return render(request, "blog/index.html", context=context)


def post_list(request):
    posts_list = Post.objects.order_by('-timestamp')
    paginated = Paginator(posts_list, per_page=4)
    page_number = request.GET.get('page')
    try:
        paginated_posts = paginated.page(page_number)
    except PageNotAnInteger:
        paginated_posts = paginated.page(1)
    except EmptyPage:
        paginated_posts = paginated.page(paginated.num_pages)
    context = {
        'posts': paginated_posts,
        'latest_posts': posts_list[0:3],
        'category_count': Post.objects.values('category__title')
        .annotate(category__count=Count('category__title'))
    }
    print(Post.objects.values('category__title').annotate(
        category__count=Count('category__title'))
    )
    return render(request, 'blog/blog.html', context=context)


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {
        "post": post
    }
    return render(request, 'blog/post.html', context=context)
