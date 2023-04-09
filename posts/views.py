from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post, Like
from .forms import PostForm


# @login_required
def post_list(request):
    latest_posts = Post.objects.order_by('-created_at')[:10]
    context = {'latest_posts': latest_posts}
    return render(request, 'posts/post_list.html', context)


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    mode = Post
    form_class = PostForm


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')


@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    # Check if the user has already liked the post
    try:
        like = Like.objects.get(post=post, user=user)
        like.delete()
    except Like.DoesNotExist:
        # Create a new like for the post
        like = Like(post=post, user=user)
        like.save()

    # Redirect back to the post detail page
    return redirect(reverse_lazy('posts:post-detail', kwargs={'pk': pk}))
