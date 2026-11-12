from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from .models import Post, Subscriber
from .forms import CommentForm
from .forms import SubscriberForm
from django.contrib import messages
from django.core import signing
from django.urls import reverse
from django.conf import settings


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

    comments = post.comments.all().order_by('-created_at')

    return render(request, 'blogapp/post_detail.html', {
        'post': post,
        'form': form,
        'comments': comments,
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

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)

    if form.is_valid():
        subscriber = form.save()

        token = signing.dumps(

            subscriber.email,

            salt='blog-subscription'

        )

        confirm_url = request.build_absolute_uri(

            reverse('blogapp:confirm_subscription', args = [token])

        )

        messages.success(

            request,

            f"Для підтвердження підписки відкрийте: {confirm_url}"

        )

        return redirect('blogapp:post_list')

    else:
        messages.warning(
                request,
                "Ця emaill-адреса вже підписана або введена некоректно."
        )

        return redirect('blogapp:post_list')
def confirm_subscription(request, token):

    try:

        email = signing.loads(

            token,

            salt='blog-subscription',

            max_age=86400

        )

        subscriber = get_object_or_404(

            Subscriber,

            email=email

        )

        subscriber.is_confirmed = True

        subscriber.save()

        messages.success(

            request,

            "Вашу підписку успішно підтверджено!"

        )

    except signing.BadSignature:

        messages.error(

            request,

            "Посилання недійсне або термін його дії закінчився."

        )

    return redirect('blogapp:post_list')