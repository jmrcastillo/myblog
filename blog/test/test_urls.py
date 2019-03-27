

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import (PostListView,
                        post_detail,
                        PostCreateView,
                        PostUpdateView,
                        PostDeleteView,
                        post_share
                        )


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolve(self):
        url = reverse('blog:post_list')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_detail_url_is_resolve(self):
        url = reverse('blog:post_detail', args=['testing-the-url'])
        self.assertEquals(resolve(url).func, post_detail)

    def test_create_url_is_resolve(self):
        url = reverse('blog:post_create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_update_url_is_resolve(self):
        url = reverse('blog:post_update', args=['testing-the-url'])
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    def test_delete_url_is_resolve(self):
        url = reverse('blog:post_delete', args=['testing-the-url'])
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)

    def test_share_url_is_resolve(self):
        url = reverse('blog:post_share', args=['3'])
        self.assertEquals(resolve(url).func, post_share)
