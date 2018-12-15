
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
# from django.views.generic.edit import CreateView
from .models import Post
from .forms import EmailPostForm
from django.core.mail import send_mail

class PostListView(ListView):
    model = Post                        # queryset = Post.objects.all()
    context_object_name = 'posts'       # can remove - object_list default in templates
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)
    return render(request, 'blog/post/detail.html', {'post': post})


# class PostCreateView(CreateView):
#     model = Post
#     template_name = 'blog/post/create.html'
#     fields = ['title', 'author', 'body']

def post_share(request, post_id):
    # retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='draft')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True

    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})
