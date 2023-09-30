from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post

NUMBER_OF_POSTS = 5


def get_base_quesryset():
    return Post.objects.select_related(
        'author',
        'location',
        'category'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def post_detail(request, post_id):
    post = get_object_or_404(
        get_base_quesryset(),
        pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def index(request):
    post_list = (get_base_quesryset()[:NUMBER_OF_POSTS])
    return render(request, 'blog/index.html', {'post_list': post_list})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug,
        is_published=True
    )
    category_page_posts = get_base_quesryset(
        ).filter(
            category__slug=category_slug
        )
    return render(
        request, 'blog/category.html',
        {'category': category,
         'post_list': category_page_posts}
    )
