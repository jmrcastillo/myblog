

from django.test import TestCase
from blog.models import Post
from django.utils import timezone
from django.contrib.auth import get_user_model


class TestPostModel(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            status='draft',
            publish=timezone.now(),   # date.today()
            created=timezone.now(),
            author=self.user
        )

    def test_absolute_url(self):
        slug = self.post.slug
        self.assertEquals(slug, 'a-good-title')

    def test_post_is_assigned_slug_on_creation(self):
        """
        Test Slug
        """
        self.assertEquals(self.post.slug, 'a-good-title')
