from django.urls import path

from blog import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('',  views.IndexView.as_view(), name="index"),
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('post/create/', login_required(views.PostCreateView.as_view()),
         name='post_create'),
    path('post/update/<int:pk>/',
         login_required(views.PostUpdateView.as_view()), name='post_update'),
    path('post/delete/<int:pk>/',
         login_required(views.PostDeleteView.as_view()), name='post_delete'),
]
