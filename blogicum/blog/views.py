from django.utils import timezone

from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category

NUMBER_OF_POSTS = 5


def get_post_object():
    return Post.objects.select_related(
               'author',
               'location',
               'category').filter(
                   is_published=True,
                   category__is_published=True,
                   pub_date__lte=timezone.now()
           )


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
               get_post_object(),
               pk=post_id)
    context = {'post': post}
    return render(request, template, context)


def index(request):
    template = 'blog/index.html'
    post_list = (get_post_object()[:NUMBER_OF_POSTS])
    context = {'post_list': post_list}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category_post = get_object_or_404(
                        Category, slug=category_slug,
                        is_published=True
                    )
    category_page_post = get_post_object().filter(category__slug=category_slug)
    context = {
              'category': category_post,
              'post_list': category_page_post}
    return render(request, template, context)
