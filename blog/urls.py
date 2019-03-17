

from django.urls import path
from .views import (post_detail,
                    PostListView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    post_share)


app_name = 'blog'
urlpatterns = [
    # post views
    # path(r'^$', post_list, name='post_list'),
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:post>/', post_detail, name='post_detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('<slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
