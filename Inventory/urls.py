from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lists/<int:id>", views.detail_list, name="detail_list"),
    path("lists", views.lists, name="lists"),
    path("create", views.create, name="create"),
]