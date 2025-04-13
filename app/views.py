from django.shortcuts import render,redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from app.forms import ContactForm
from blog.models import Post
# ======================================================================================================================
def index(request):
    posts = Post.objects.filter(status=1)
    # ==================================================================================================================
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts':posts}
    return render(request, 'website/index.html', context)
# ======================================================================================================================
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your message has been sent.')
            form.save()
        else:
            messages.error(request, 'Please correct the error below.')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})
# ======================================================================================================================