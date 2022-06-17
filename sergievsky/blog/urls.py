from django.urls import path
from .views import PostListView, PostDetailView, PostUpdateView, PostDeleteView


urlpatterns = [
    path(
        'list',
        PostListView.as_view(),
        name='list_posts'
    ),
    path(
        'post/<slug:slug>/update',
        PostUpdateView.as_view(),
        name='post_update'
    ),
    path(
        'post/<slug:slug>',
        PostDetailView.as_view(),
        name='post_details'
    ),
    path(
        'post/<slug:slug>/delete',
        PostDeleteView.as_view(),
        name='post_delete'
    )
]
