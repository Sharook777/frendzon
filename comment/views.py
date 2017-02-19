from django.shortcuts import render, redirect, get_object_or_404

from comment.models import Comment
from feeds.models import Post
from django.contrib import messages

def comment(request, id=None):
    if not request.user.is_authenticated():
        return redirect("home")
    if request.method == 'POST':
        content = request.POST.get("post")
        post_detail = get_object_or_404(Post, pk=id)
        Comment.objects.create(user=request.user, post=post_detail, content=content).save()
        Comment.objects.count_comment(post_detail)
        return redirect("detail", id)
    
    
def delete_comment(request, id=None):
    if not request.user.is_authenticated():
        return redirect("home")
    comment_detail = get_object_or_404(Comment, pk=id)
    if request.user == comment_detail.user:
        comment_detail.delete()
        Comment.objects.count_comment(comment_detail.post, count=-1)
        messages.success(request, "Successfully Deleted")
    return redirect("detail", comment_detail.post)