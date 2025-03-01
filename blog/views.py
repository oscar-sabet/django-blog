from django.shortcuts import render
from django.views import generic
from .models import Post

# from django.http import HttpResponse


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(author=2).filter(status=1)
    # .order_by("-created_on")
    template_name = "post_list.html"


# def my_blog(request):
#     return HttpResponse(
#         "Hello, world. You're at the blog."
#     )  # This is the view for the blog index page.
