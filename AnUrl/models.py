from django.conf import settings
from django.db import models
from .utils import short_code_generator,create_shortcode

SHORTCODE_MAX=getattr(settings,"SHORTCODE_MAX",15)

class AnasUrlManager(models.Manager):
	def all(self,*args,**kwargs):
		qs_main=super(AnasUrlManager,self).all(*args,**kwargs)
		qs=qs_main.filter(active=True)
		return qs
	def refresh_shortcode(self,items=None):
		qs=AnasUrl.objects.filter(id__gte=1)
		if items is not None and isinstance(items,int):
			qs=qs.order_by('-id')[:items]
		new_codes=0
		for q in qs:
			q.shortcode=create_shortcode(q)
			print(q.id)
			q.save()
			new_codes+=1
		return "New codes made: {i}".format(i=new_codes)
# Create your models here.

class AnasUrl(models.Model):
	url=models.CharField(max_length=300,)
	shortcode=models.CharField(max_length=SHORTCODE_MAX,unique=True,blank=True)
	updated=models.DateTimeField(auto_now=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	active =models.BooleanField(default=True)

	objects=AnasUrlManager()

	def save(self,*args,**kwargs):
		if self.shortcode is None or self.shortcode=="":
			self.shortcode=create_shortcode(self)
		super(AnasUrl,self).save(*args,**kwargs)

	def __str__(self):
		return str(self.url)
	def __unicode__(self):
		return str(self.url)


		