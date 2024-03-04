from django.urls import path

from social_network.apps import SocialNetworkConfig
from rest_framework.routers import DefaultRouter

from social_network.views import PostCreateAPIView, PostListAPIView, PostRetrieveAPIView, PostUpdateAPIView, \
    PostDestroyAPIView, CommentCreateAPIView, CommentListAPIView, CommentRetrieveAPIView, CommentUpdateAPIView, \
    CommentDestroyAPIView

app_name = SocialNetworkConfig.name

urlpatterns = [
    path('post/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('post/', PostListAPIView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostRetrieveAPIView.as_view(), name='post-get'),
    path('post/update/<int:pk>/', PostUpdateAPIView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostDestroyAPIView.as_view(), name='post-delete'),

    path('comment/create/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('comment/', CommentListAPIView.as_view(), name='comment-list'),
    path('comment/<int:pk>/', CommentRetrieveAPIView.as_view(), name='comment-get'),
    path('comment/update/<int:pk>/', CommentUpdateAPIView.as_view(), name='comment-update'),
    path('comment/delete/<int:pk>/', CommentDestroyAPIView.as_view(), name='comment-delete'),
]