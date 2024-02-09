from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.postobjects.all()
    

class PostDetail(generics.RetrieveDestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.postobjects.all()