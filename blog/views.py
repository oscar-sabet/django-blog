from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# from django.http import HttpResponse


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    # filter(author=2).filter(status=1)
    # .order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    template_name = "blog/post_detail.html"
    post = Post.objects.get(slug=slug)
    return render(request, template_name, {"post": post})


# def my_blog(request):
#     return HttpResponse(
#         "Hello, world. You're at the blog."
#     )  # This is the view for the blog index page.
