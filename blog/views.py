from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def index(request, page):
    posts_list = Post.objects.order_by('-publish_date').filter(
        publish_date__lte=timezone.now(), hidden=False)
    paginator = Paginator(posts_list, 3)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'posts': posts})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if (post.hidden or post.publish_date > timezone.now()) and not request.user.is_staff:
        raise PermissionDenied
    return render(request, 'blog/post.html', {'post': post})
