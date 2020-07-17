from django.urls import path

from blog import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('search/', views.SearchView.as_view(), name='search')

]
