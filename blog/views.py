

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail


class PostListView(ListView):
    model = Post                        # queryset = Post.objects.all()
    context_object_name = 'posts'   # can remove - object_list default tmplates
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)

    # Comment to blog post
    # List of active comments for this post
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            # Create comment object but don't save to db yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the db
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {
                                                'post': post,
                                                'comments': comments,
                                                'comment_form': comment_form
                                                    })


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post/create.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        """
        required author before to submit form
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Update post by User
    """
    model = Post
    template_name = 'blog/post/create.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        """
        required author before to submit form
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Test if the user is equal to author
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        """
        Test if the user is equal to author
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


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
            subject = '{} ({}) recommends you reading "{}"'.format(
                    cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(
                    post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True

    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})
