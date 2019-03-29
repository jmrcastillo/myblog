

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from blog.models import Post


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('blog:post_list')
        self.detail_url = reverse('blog:post_detail', args=['a-good-title'])

        # create user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secret'
        )

        # create post
        self.post = Post.objects.create(
                                    title='A good title',
                                    slug='A-good-title',
                                    body='Nice body content',
                                    status='draft',
                                    publish=timezone.now(),   # date.today()
                                    created=timezone.now(),
                                    author=self.user
                                    )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(self.post.title, 'A good title')
        self.assertEqual(str(self.post.author), 'testuser')
        self.assertEqual(self.post.body, 'Nice body content')
        # self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_blog_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'blog/post/list.html')

    def test_blog_detail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'blog/post/detail.html')
