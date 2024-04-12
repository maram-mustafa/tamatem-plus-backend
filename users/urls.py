from django.urls import path

from users.views import UserCreateView

urlpatterns = [path("users/", UserCreateView.as_view(), name="UserListCreateView")]
