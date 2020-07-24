from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, View

from blog.models import Newsletter, Post


class IndexView(View):
    """Index view, displays home page with the latest posts

    Args:
        View: [Django View]
    """

    def get(self, request, *args, **kwargs):
        featured_posts = Post.objects.filter(featured=True)[0:3]
        latest_posts = Post.objects.order_by('-timestamp')[0:3]
        context = {
            'featured_posts': featured_posts,
            'latest_posts': latest_posts
        }
        return render(request, 'blog/index.html', context=context)

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        newsletter = Newsletter()
        newsletter.email = email
        newsletter.save()
        messages.info(request, 'Successfully subscribed!')
        return redirect('index')


class PostDetailView(DetailView):
    """Post Detail view, displays post details

    Args:
        DetailView: Django Detail View

    Returns:
        [type]: [description]
    """

    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_posts"] = Post.objects.all().order_by(
            '-timestamp')[0:3]
        context["category_count"] = Post.objects.values(
            'category__title') \
            .annotate(category__count=Count('category__title'))
        return context


class PostListView(ListView):
    """Post List View, displays posts as a list with pagination

    Args:
        ListView: Django List View

    Returns:
        context: context
    """
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_posts"] = Post.objects.all().order_by(
            '-timestamp')[0:3]
        context["category_count"] = Post.objects.values(
            'category__title') \
            .annotate(category__count=Count('category__title'))
        return context


class SearchView(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        search_result = Post.objects.filter(
            Q(title__icontains=q) | Q(overview__icontains=q)).all()
        context = {
            "search_result": search_result
        }
        return render(request, 'blog/search.html', context=context)
