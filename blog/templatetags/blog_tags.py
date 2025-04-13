from django import template
from blog.models import Post, Category

register = template.Library()
# ======================================================================================================================
@register.inclusion_tag('blog/tags.html')
def tags():
    posts = Post.objects.filter(status=1)
    return {'posts': posts}
# ======================================================================================================================
@register.inclusion_tag('blog/popular.html')
def popular():
    posts = Post.objects.filter(status=1)[0:4]
    return {'posts': posts}
# ======================================================================================================================
@register.inclusion_tag('website/category.html')
def category():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    category_dict = {}
    for name in categories:
        category_dict[name]=name
    return {'category_dict': category_dict}
# ======================================================================================================================
@register.inclusion_tag('website/most_viewed_posts.html')
def most_viewed_posts():
    posts = Post.objects.filter(status=1)[0:3]
    return {'posts': posts}
# ======================================================================================================================
@register.inclusion_tag('website/last_modified_posts.html')
def last_modified_posts(limit=6):
    posts = Post.objects.filter(status=1).order_by('-updated_date')[:limit]
    return {'posts': posts}
# ======================================================================================================================