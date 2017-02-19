from django.contrib import admin
from .models import Post, Post_like

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["user","timestamp","update"]
    list_filtering = ["user"]
    search_fields = ["user"]
    
    class Meta:
        model = Post

class LikeModelAdmin(admin.ModelAdmin):
    list_display = ["user", "post"]
    class Meta:
        model = Post_like
        
admin.site.register(Post, PostModelAdmin)
admin.site.register(Post_like, LikeModelAdmin)