from feeds.models import Post

import random
import string
def slug_for_user(size=5, chars= string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range (size))


def create_slug(instance=None, size=8):
    new_slug = slug_for_user(size=size)
    queryset_exist = Post.objects.filter(slug=new_slug).exists()
    if queryset_exist:
        return slug_for_user(size=size)
    return new_slug