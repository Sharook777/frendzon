from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from .models import Post, Post_like
from .forms import PostForm
from .utils import create_slug
from user.models import Users
from comment.models import Comment, Replay
from django.contrib.contenttypes.models import ContentType


def list_post(request):
    if not request.user.is_authenticated():
        return redirect("home")
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    join_date = request.user.date_joined
    queryset = Post.objects.filter(timestamp__gte=join_date)
    
    from django.db.models import Q
    query = request.GET.get('q')
    if query:
        queryset = Post.objects.filter(Q(content__icontains=query))

    paginator = Paginator(queryset,10) 
    page_request = 'page'
    page = request.GET.get(page_request)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages) 
    temp = Post_like.objects.filter(user=request.user)
    like = []
    for l in temp:
        t1 = Post.objects.get(pk=l)
        like.append(t1.slug)
    profile = Users.objects.get(user=request.user)
    
    context = {  
        'objects':pages,
        "title":"list ",
        "like":like,
        "page_request":page_request,
        "profile":profile,
        "home":"active",
        }
    return render(request, "list.html", context)


   
def create_post(request):
    if not request.user.is_authenticated():
        return redirect("home")

    if request.method == "POST":
        content = request.POST.get("post")
        image = request.FILES.get("image")
        slug = create_slug()
       
        Post.objects.create(user=request.user, slug=slug, content=content, image=image).save()
      
        return redirect("list")
    return render(request, "profile.html",)


def detail_post(request, id=None):
    if not request.user.is_authenticated():
        return redirect("home")
    post_detail = get_object_or_404(Post, pk=id)
    print("post detail from detailview",post_detail)
    try:
        post_like = Post_like.objects.get(user=request.user, post=post_detail)
        if post_like:
            like = True
    except:
        like = False
    content_type = ContentType.objects.get_for_model(Post)
    print("content type",content_type)
    comments = Comment.objects.filter( post=post_detail)
    context = {
        'object':post_detail,
        'comments':comments,
        "likes":post_detail.likes,
        "liked":like,
        }
    return render(request, "detail.html", context)

def update_post(request, id=None):
    if not request.user.is_authenticated():
        return redirect("home")
    post_detail = get_object_or_404(Post, pk=id)
    if request.user == post_detail.user:
        form = PostForm(request.POST or None, request.FILES or None, instance=post_detail)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "<a href=#>Successfully Updated</a>")
            return redirect("detail", post_detail.pk)
        else:
            context = {
                'object':post_detail,
                'form':form,
                'title':"Edit Post",
                }
        return render(request, "update.html", context)
    return redirect("detail", post_detail.pk)


def delete_post(request, id=None):
    if not request.user.is_authenticated():
        return redirect("home")
    post_detail = get_object_or_404(Post, pk=id)
    if request.user == post_detail.user:
        post_detail.delete()
        messages.success(request, "Successfully Deleted")
    return redirect("list")


def likes(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    new_like, created = Post_like.objects.get_or_create(user=request.user, post=post_detail)
    if not created: 
        new_like.delete()
        Post_like.objects.count_likes(post_detail, -1)
    else:
        new_like.like = "L"
        new_like.save()
        Post_like.objects.count_likes(post_detail, 1)
        
    print(request)
    return redirect("list")


def chats(request):
    if not request.user.is_authenticated():
        return redirect("home")
    return render(request, "chat.html")


