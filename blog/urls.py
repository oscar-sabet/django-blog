from . import views
from django.urls import path

# from . import views


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    # path("posts/", views.PostList.as_view(), name="home"),
]
