from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from ..models import Cocktail, Post, Comment

from .serializers import (
    CocktailSerializer,
    CocktailCreateSerializer,
    CreateUserSerializer,
    PostSerializer,
    CommentSerializer)

from django.contrib.auth import get_user_model

User = get_user_model()

class CocktailCreateAPIView(CreateAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailCreateSerializer

class CocktailListAPIView(ListAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

class CocktailRetrieveAPIView(RetrieveAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

class CocktailUpdateAPIView(UpdateAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

class CocktailDeleteAPIView(DestroyAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserCreateAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer