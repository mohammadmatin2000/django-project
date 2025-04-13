from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Post,Category

# ======================================================================================================================
def blog(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('author_name'):
        posts = posts.filter(author__username=kwargs.get('author_name'))
    if kwargs.get('category_name'):
        posts = posts.filter(category__name=kwargs.get('category_name'))
    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name__in=[kwargs.get('tag_name')])
    # ==================================================================================================================
    page=request.GET.get('page',1)
    paginator = Paginator(posts,3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # ==================================================================================================================
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)
# ======================================================================================================================
def single(request,pid):
    post = Post.objects.get(id=pid)
    posts = Post.objects.filter(status=1)
    context = {'post':post,'posts':posts}
    return render(request,'blog/single.html',context)
# ======================================================================================================================
def base(request):
    category = Category.objects.all()
    context = {'category':category}
    return render(request,'blog/base.html',context)
# ======================================================================================================================