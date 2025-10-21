from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Blog, Post, Tag


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                    return data
                else:
                    raise serializers.ValidationError("Usuario inactivo")
            else:
                raise serializers.ValidationError("Credenciales inválidas")
        else:
            raise serializers.ValidationError("Debe proporcionar username y password")

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password_confirm']
    
    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user

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