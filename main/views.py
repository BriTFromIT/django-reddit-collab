from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


# Create your views here.
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
