from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import redirect, render

from accounts.forms import UserRegistrationForm
from accounts.models import Profile
