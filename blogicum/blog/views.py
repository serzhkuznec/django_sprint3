import datetime
from django.shortcuts import render, get_object_or_404, get_list_or_404
from blog.models import Post, Category


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related('author', 'location', 'category')
        .filter(is_published=True, category__is_published=True),
        pk=post_id,
        pub_date__date__lt=datetime.datetime.now()
    )
    context = {
        'post': post
    }
    return render(request, template, context)


def index(request):
    template = 'blog/index.html'
    post_list = (
        Post.objects.select_related('author', 'location', 'category')
        .filter(is_published=True,
                category__is_published=True,
                pub_date__date__lt=datetime.datetime.now())[0:5]
    )
    context = {
        'post_list': post_list
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category_page_post = get_list_or_404(
        Post.objects.select_related('author', 'location', 'category')
        .filter(is_published=True,
                category__slug=category_slug,
                category__is_published=True,
                pub_date__date__lt=datetime.datetime.now())
    )
    category_slug = Category.objects.get(slug=category_slug)
    context = {
        'category': category_slug,
        'post_list': category_page_post
    }
    return render(request, template, context)
