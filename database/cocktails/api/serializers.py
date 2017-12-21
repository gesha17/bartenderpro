from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()
from ..models import(
    Cocktail,
    Comment,
    Post)

class CocktailSerializer(ModelSerializer):
    class Meta:
        model = Cocktail
        fields = [
            'id',
            'name',
            'category',
            'ingredients',
            'recipe',
            'image',
            'description',
            'difficulty',
        ]

class CocktailCreateSerializer(ModelSerializer):
    class Meta:
        model = Cocktail
        fields = [
            #'id',
            'name',
            'category',
            'ingredients',
            'recipe',
            'image',
            'description',
            'difficulty',
        ]

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'user',
            'cocktail',
            'likes',
            'dislikes',
            'comment',
            'date',
        ]

class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        extra_kwargs = {'password': {'write_only':True}}

        def validate(self, data):
            return data
        def create(self,validated_data):
            username = validated_data['username']
            password = validated_data['password']
            user_obj = User(username = username)
            user_obj.set_password(password)
            user_obj.save()
            return validated_data
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields=[
            'user',
            'cocktail',
            'comment',
        ]

        def perform_create(self,serializer):
            serializer.save()
        """"def create(self,validated_data):
            username = validated_data['username']
            cocktail = validated_data['cocktail']
            comment = validated_data['comment']
            post = Post(username, cocktail, comment)
            post.save()
            return validated_data
        """""