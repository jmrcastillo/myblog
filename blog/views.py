
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
# from django.views.generic.edit import CreateView
from .models import Post


class PostListView(ListView):
    model = Post 						# queryset = Post.objects.all()
    context_object_name = 'posts'		# can remove - object_list default in templates
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):

    post = get_object_or_404(Post, slug=post,
                             status='draft',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


# class PostCreateView(CreateView):
#     model = Post
#     template_name = 'blog/post/create.html'
#     fields = ['title', 'author', 'body']