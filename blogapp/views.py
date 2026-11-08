from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from .models import Post
from .forms import CommentForm


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(
        request,
        'blogapp/post_list.html',
        {'posts': posts}
    )

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f'/admin/login/?next={request.path}')

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(request.path)
    else:
        form = CommentForm()

    return render(request, 'blogapp/post_detail.html', {
        'post': post,
        'form': form,

    })
def profile_detail(request, user_id):
    User = get_user_model()
    author = get_object_or_404(User, id=user_id)

    posts = Post.objects.filter(
        author=author
    ).order_by('-created_at')
    return render(
        request,
        'blogapp/profile_detail.html',
        {
            'author': author,
            'posts': posts
        }
    )