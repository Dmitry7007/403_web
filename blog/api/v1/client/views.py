from api.v1.client.serializers.blog_serializer import ArticleSerializer, CommentSerializer, CategorySerializer
from rest_framework import viewsets
from main.models import Article, Comment, Category

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer