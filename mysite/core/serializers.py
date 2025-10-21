from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog, Post, Tag

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class BlogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Blog
        fields = ['id', 'title', 'bio', 'user', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    blog = BlogSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'content', 'excerpt', 
            'cover', 'tags', 'is_published', 'created_at', 
            'updated_at', 'published_at', 'blog'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title', 'content', 'excerpt', 'cover', 
            'tags', 'is_published'
        ]