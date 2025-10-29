from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from ..models import Blog, Post, Tag

class APITestCase(APITestCase):
    """Test API endpoints"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.blog = Blog.objects.create(
            user=self.user,
            title='Test Blog'
        )
    
    def test_user_registration(self):
        """
        Test user registration endpoint.
        
        PURPOSE: Verifica que el endpoint de registro de usuarios funciona
        correctamente. Debe crear un nuevo usuario y devolver un token
        de autenticación para uso inmediato.
        """
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123',
            'password_confirm': 'newpass123'
        }
        response = self.client.post('/api/users/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
    
    def test_user_login(self):
        """
        Test user login endpoint.
        
        PURPOSE: Verifica que el endpoint de login de usuarios funciona
        correctamente. Debe autenticar al usuario y devolver un token
        de autenticación para las siguientes peticiones.
        """
        data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        response = self.client.post('/api/users/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
    
    def test_post_creation(self):
        """
        Test post creation endpoint.
        
        PURPOSE: Verifica que el endpoint de creación de posts funciona
        correctamente. Un usuario autenticado debe poder crear posts
        en su blog con todos los campos necesarios.
        """
        data = {
            'title': 'Test Post',
            'content': '<p>Test content</p>',
            'excerpt': 'Test excerpt',
            'is_published': True
        }
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Post')
    
    def test_post_list(self):
        """
        Test post list endpoint.
        
        PURPOSE: Verifica que el endpoint de listado de posts funciona
        correctamente. Debe devolver todos los posts disponibles con
        paginación (por eso se usa response.data['results']).
        """
        Post.objects.create(
            blog=self.blog,
            title='Test Post',
            content='<p>Test content</p>'
        )
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_post_permissions(self):
        """
        Test that users can only modify their own posts.
        
        PURPOSE: Verifica que el sistema de permisos funciona correctamente
        en la API. Un usuario NO debe poder modificar posts de otros usuarios,
        debe recibir un error 403 Forbidden.
        """
        # Create another user
        other_user = User.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='otherpass123'
        )
        other_blog = Blog.objects.create(
            user=other_user,
            title='Other Blog'
        )
        other_post = Post.objects.create(
            blog=other_blog,
            title='Other Post',
            content='<p>Other content</p>'
        )
        
        # Try to update other user's post
        data = {'title': 'Updated Title'}
        response = self.client.put(f'/api/posts/{other_post.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_tag_creation(self):
        """
        Test tag creation endpoint.
        
        PURPOSE: Verifica que solo los superusuarios pueden crear tags
        a través de la API. Los tags son elementos globales del sistema,
        por lo que solo los administradores pueden crearlos.
        """
        # Create superuser for tag creation (only superusers can create tags)
        superuser = User.objects.create_superuser(
            username='superuser',
            email='super@example.com',
            password='superpass123'
        )
        superuser_token = Token.objects.create(user=superuser)
        
        # Use superuser credentials
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + superuser_token.key)
        
        data = {'name': 'Django'}
        response = self.client.post('/api/tags/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Django')
    
    def test_published_posts_filter(self):
        """
        Test published posts filter.
        
        PURPOSE: Verifica que el filtro de posts publicados funciona
        correctamente. Solo debe devolver posts con is_published=True,
        excluyendo los borradores (is_published=False).
        """
        # Create published and unpublished posts
        Post.objects.create(
            blog=self.blog,
            title='Published Post',
            content='<p>Published content</p>',
            is_published=True
        )
        Post.objects.create(
            blog=self.blog,
            title='Unpublished Post',
            content='<p>Unpublished content</p>',
            is_published=False
        )
        
        response = self.client.get('/api/posts/published/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Published Post')
    
    def test_posts_by_tag_filter(self):
        """
        Test posts by tag filter.
        
        PURPOSE: Verifica que el filtro de posts por tag funciona
        correctamente. Debe devolver solo los posts que tienen
        el tag especificado en el parámetro de consulta.
        """
        tag = Tag.objects.create(name='Django')
        post = Post.objects.create(
            blog=self.blog,
            title='Django Post',
            content='<p>Django content</p>'
        )
        post.tags.add(tag)
        
        response = self.client.get('/api/posts/by_tag/?tag=Django')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Django Post')