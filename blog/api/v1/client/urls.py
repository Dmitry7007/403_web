from django.urls import path, include
from rest_framework import routers
from api.v1.client.views import ArticleViewSet, CommentViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]