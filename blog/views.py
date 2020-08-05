# -*- coding: utf-8 -*-
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)

from accounts.models import Author
from blog.forms import CommentForm, PostForm
from blog.models import Category, Newsletter, Post


class IndexView(View):
    def get(self, request, *args, **kwargs):
        featured_posts = Post.objects.filter(featured=True)[0:3]
        latest_posts = Post.objects.order_by("-timestamp")[0:3]
        context = {"featured_posts": featured_posts, "latest_posts": latest_posts}
        return render(request, "blog/index.html", context=context)

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        newsletter = Newsletter()
        newsletter.email = email
        newsletter.save()
        messages.info(request, "Successfully subscribed!")
        return redirect("index")


class PostDetailView(DetailView):

    model = Post
    template_name = "blog/post_detail.html"
    _comment_form = CommentForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_posts"] = Post.objects.all().order_by("-timestamp")[0:3]
        context["categories"] = Category.objects.all()
        context["comment_form"] = self._comment_form
        return context

    def post(self, request, *args, **kwargs):
        _post = self.get_object()
        _comment_form = CommentForm(request.POST)
        if _comment_form.is_valid():
            _comment_form.instance.user = request.user.author
            _comment_form.instance.post = _post
            _comment_form.save()
            return redirect(_post)


class PostListView(ListView):

    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_posts"] = Post.objects.all().order_by("-timestamp")[0:3]
        context["categories"] = Category.objects.all()
        return context


class SearchView(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get("q", "")
        search_result = Post.objects.filter(
            Q(title__icontains=q) | Q(overview__icontains=q)
        ).all()
        context = {"search_result": search_result}
        return render(request, "blog/search.html", context=context)


class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_create.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = Author.objects.filter(user=self.request.user).first()
        form.save()
        return redirect(reverse("post_detail", kwargs={"slug": form.instance.slug}))


class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    form_class = PostForm

    def form_valid(self, form):
        if form.instance.author == self.request.user.author:
            form.save()
            return redirect(reverse("post_detail", kwargs={"slug": form.instance.slug}))


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("index")
