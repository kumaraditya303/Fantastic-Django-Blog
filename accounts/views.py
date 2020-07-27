from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import CreateView, UpdateView

from accounts.forms import UserRegistrationForm, AuthorForm
from accounts.models import Author


class AuthorCreateView(CreateView):
    template_name = 'accounts/author_form.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        Author.objects.create(user=user)
        return super().form_valid(form)


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = "accounts/author_update.html"
    form_class = AuthorForm
    success_url = reverse_lazy('account_update')
