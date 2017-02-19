import random
import string
#from user.models import Shortcode

from django.conf import settings
shortcode_min = getattr(settings, "SHORTCODE_MIN", 15)


def code_generator(size=shortcode_min,
                   chars= string.ascii_uppercase + string.digits +
                   string.ascii_lowercase):       # chars="abcdefghijklmnopqrstuvwxyz123456789"
    #new_code = ''
    #for _ in range(size):        # _ is used because we never using the variable its just for iteration
        #new_code += random.choice(chars) 
    #return new_code
    return ''.join(random.choice(chars) for _ in range (size))

def create_shortcode(instance, size=shortcode_min):
    #print(shortcode_min)
    new_code = code_generator(size=size)
    #print(instance)
    #print(instance.__class__)
    #print(instance.__class__.__name__)
    
    #post = instance.__class__          # get class of instance its same as importing class
    #queryset_exist = Shortcode.objects.filter(shortcode=new_code).exists() # if the newcode is exist on shortcode database then returns true
    
    #if queryset_exist:
        #return create_shortcode(size=size)      # if the new shortcode is already exist in db then continue to create new shortcode by stopping current function and starting newone
    
    return new_code
