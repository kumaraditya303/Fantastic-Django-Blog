from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User
# Create your tests here.
class BlogTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='test',password='test')
        Post.objects.create(title='Lorem ipsum', content='Lorem ipsum dolor amit',
        author = user
        )

    def test_home_page(self):
        post = Post.objects.get(title__startswith="Lorem")