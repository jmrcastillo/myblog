

from django.conf.urls import url
from .views import post_detail, PostListView

urlpatterns = [
    # post views
    # url(r'^$', post_list, name='post_list'),
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^(?P<post>[\w-]+)/$',
        post_detail,
        name='post_detail'),
    # url(r'^post/create$', PostCreateView.as_view(), name='post_create')
]
