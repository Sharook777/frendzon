from django.db import models

from django.contrib.auth.models import User
from feeds.models import Post


class CommentManager(models.Manager):
    def count_comment(self, instance, count=1):
        if isinstance(instance, Post):
            instance.comments += count
            instance.save()
            return instance.comments
        return None
    


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    objects = CommentManager()

    def __str__(self):
        return str(self.user)
    
    class Meta:
        ordering = ["-timestamp"]
    
class Replay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, default=None, on_delete=models.CASCADE)
    content = models.TextField()
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return str(self.user)
