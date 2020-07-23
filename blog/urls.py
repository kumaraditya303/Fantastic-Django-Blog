from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:id>', views.post_detail, name='post_detail')

]
