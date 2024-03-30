from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import Post
from blog.views import post_list, user_post_list, post_detail, user_post_detail, post_new, post_edit, post_delete

class PostModelTest(TestCase):
    def test_publish(self):
        author = User.objects.create(username='Feeru')
        post = Post.objects.create(author=author, title='Продажа гаража', text='Продам гараж')
        post.publish()
        self.assertIsNotNone(post.published_date)

class ViewsTest(TestCase):
    def test_post_list_view(self):
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view(self):
        author = User.objects.create(username='Feeru')
        post = Post.objects.create(author=author, title='Продажа гаража', text='Продам гараж')
        response = self.client.get(f'/user/post/{post.pk}/')
        self.assertEqual(response.status_code, 200)