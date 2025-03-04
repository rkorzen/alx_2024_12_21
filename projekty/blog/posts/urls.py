from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
app_name = "posts"
urlpatterns = [
    path("", views.posts_list, name="list"),
    path("login/", views.login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<int:post_id>/", views.post_details, name="details"),
    path("new/", views.post_create, name="create"),

    path("api/v1/posts", views.posts_list_api, name="posts_list_api"),

]
