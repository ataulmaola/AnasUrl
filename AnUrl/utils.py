import random
import string
from django.conf import settings


SHORTCODE_MIN=getattr(settings,"SHORTCODE_MIN",6)

def short_code_generator(size=SHORTCODE_MIN,chars=string.ascii_lowercase+string.digits):
	newcode=''
	for _ in range(size):
		newcode+=random.choice(chars)
	return newcode


def create_shortcode(instance,size=SHORTCODE_MIN):
	new_code=short_code_generator(size=size)
	UtilsClass=instance.__class__
	qs_exists=UtilsClass.objects.filter(shortcode=new_code).exists()
	if qs_exists:
		return create_shortcode(size=size)
	return new_code