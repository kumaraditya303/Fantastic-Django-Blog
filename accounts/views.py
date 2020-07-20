from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import redirect, render

from accounts.forms import UserRegistrationForm
from accounts.models import Profile


def author(request, author):
    author = serializers.serialize(
        "json", [Profile.objects.filter(user=author).first()])
    return JsonResponse(author, safe=False)


def register(request):
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your account has been created successfully! You may login!')
            return redirect("index")
    form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
