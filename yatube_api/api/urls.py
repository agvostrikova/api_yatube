from django.urls import include, path

from rest_framework import routers
from rest_framework.authtoken import views

from .views import GroupViewSet, PostViewSet, CommentViewSet


router = routers.DefaultRouter()

router.register('groups', GroupViewSet, basename='group')
router.register('posts', PostViewSet, basename='post')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment'
)


urlpatterns = [
    path(
        'v1/',
        include(
            [
                path('', include(router.urls)),
                path('api-token-auth/', views.obtain_auth_token),
            ]
        ),
    ),
]
