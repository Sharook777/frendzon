from user.models import Users

import random
import string
def slug_for_user(size=5, chars= string.digits):
    return ''.join(random.choice(chars) for _ in range (size))


def create_slug(instance=None, size=5):
    new_slug = slug_for_user(size=size)
    queryset_exist = Users.objects.filter(slug=new_slug).exists()
    if queryset_exist:
        return slug_for_user(size=size)
    return new_slug