from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from user.models import Users

class PostManager(models.Manager):
    def count_likes(self, instance, count):
        if isinstance(instance, Post):
            instance.likes += count
            instance.save()
            return instance.likes
        return None
        
from social.utils import create_shortcode     
def upload_imagesTo(instance, filename):
    user=User.objects.get(username=instance.user)
    filename, extension = filename.split(".")
    name = create_shortcode(instance)
    return "%s/post/%s.%s" %(user.username, name, extension)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=10, primary_key=True,unique=True)
    content = models.TextField()
    image = models.FileField(upload_to=upload_imagesTo, null=True, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
   
    
   
    def __str__(self):
        return str(self.slug )
    
    def get_absolute_url(self):
        url = Users.objects.get(user=self.user)
        return reverse("profile", kwargs={ "member":url.pk })
  
    class Meta:
        ordering = ["-timestamp"]

class Post_like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.CharField(max_length=10, default=None, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    objects = PostManager()
    
    def __str__(self):
        return str(self.post)
           
        
    class Meta:
        ordering = ["post", "-updated",]        
