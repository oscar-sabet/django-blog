from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def my_blog(request):
    return HttpResponse(
        "Hello, world. You're at the blog."
    )  # This is the view for the blog index page.
