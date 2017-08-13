from django.http import HttpResponse
from django.shortcuts import render

def Url_Redirect_View(request,shortcode=None,*args,**kwargs):
	print(args)
	print(kwargs)
	return HttpResponse("Hello")


# Create your views here.
