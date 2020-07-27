from django.urls import path
from django.contrib.auth.decorators import login_required
from accounts import views
urlpatterns = [
    path('accounts/register/', views.AuthorCreateView.as_view(),
         name='accounts_register'),
    path("accounts/update/<pk>",
         login_required(views.AuthorUpdateView.as_view()), name="accounts_update")
]
