from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args,**kwargs):
    return HttpResponse("<h1>Hello World!</h1>")

def contact_view(*args,**kwargs):
    return HttpResponse("<h1>Contact page</h1>")

def about_view(*args,**kwargs):
    return HttpResponse("<h1>About page</h1>")

def social_view(*args,**kwargs):
    return HttpResponse("<h1>Social page</h1>")