# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

from accounts.forms import AuthorForm, UserForm, UserUpdateForm
from accounts.models import Author
from blog.models import Newsletter


class AuthorCreateView(CreateView):
    template_name = "accounts/author_form.html"
    form_class = UserForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        Author.objects.create(user=user)
        Newsletter.objects.create(email=user.email)
        return super().form_valid(form)


class AuthorUpdateView(View):
    def get(self, request, *args, **kwargs):
        author_form = AuthorForm(instance=request.user.author)
        user_form = UserUpdateForm(instance=request.user)
        context = {"author_form": author_form, "user_form": user_form}
        return render(request, "accounts/author_update.html", context=context)

    def post(self, request, *args, **kwargs):
        author_form = AuthorForm(
            request.POST, request.FILES, instance=request.user.author
        )
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if author_form.is_valid() and user_form.is_valid():
            user_form.save()
            author_form.save()
        return redirect("accounts_update")
