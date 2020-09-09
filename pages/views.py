from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"home.html",{})
    #return HttpResponse("<h1>Contact page</h1>")

def contact_view(request, *args,**kwargs):
    return render(request,"contact.html",{})

def about_view(request, *args,**kwargs):
    my_context = {
        "my_text":"This is about us",
        "my_number":12345,
        "my_list": [ 123,456,789 ]
    }
    return render(request,"about.html", my_context)

def social_view(request, *args,**kwargs):
    return render(request,"social.html",{})