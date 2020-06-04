from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import Post
def homepage(request):

    post = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post,4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'heyfemifront.html', {'posts':posts, 'page':page})
def content(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    wordList = post.Content.split("NP/")
    return render(request, 'content.html', {'post':post, 'wordList': wordList})
def category(request, category_id):
    categories = Category.objects.get(pk=category_id)
    cates = Category.objects.all()
    category_posts = Post.objects.filter(category=categories)
    return render(request, 'category.html', {'cates':cates,'categories':categories,'category_posts':category_posts})
