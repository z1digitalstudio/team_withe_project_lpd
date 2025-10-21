from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Blog, Post, Tag
from .serializers import (
    UserSerializer, BlogSerializer, PostSerializer, 
    PostCreateSerializer, TagSerializer, UserRegistrationSerializer, UserLoginSerializer
)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):
        """Registro de nuevos usuarios"""
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Crear blog automáticamente para el nuevo usuario
            Blog.objects.create(
                user=user,
                title=f"Blog de {user.username}"
            )
            # Crear token para el usuario
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': UserSerializer(user).data,
                'token': token.key,
                'message': 'Usuario registrado exitosamente'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def login(self, request):
        """Login de usuarios"""
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': UserSerializer(user).data,
                'token': token.key,
                'message': 'Login exitoso'
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Blog.objects.all()
        return Blog.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(blog__user=self.request.user)
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PostCreateSerializer
        return PostSerializer
    
    def perform_create(self, serializer):
        # Asignar automáticamente el blog del usuario
        user_blog = Blog.objects.filter(user=self.request.user).first()
        if user_blog:
            serializer.save(blog=user_blog)
        else:
            # Crear blog automáticamente si no existe
            blog = Blog.objects.create(
                user=self.request.user,
                title=f"Blog de {self.request.user.username}"
            )
            serializer.save(blog=blog)
    
    @action(detail=False, methods=['get'])
    def published(self, request):
        """Endpoint para obtener solo posts publicados"""
        posts = self.get_queryset().filter(is_published=True)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_tag(self, request):
        """Endpoint para filtrar posts por tag"""
        tag_name = request.query_params.get('tag', None)
        if tag_name:
            posts = self.get_queryset().filter(tags__name__icontains=tag_name)
        else:
            posts = self.get_queryset()
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)