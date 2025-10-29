from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from ..models import Blog, Post, Tag

class AdminTest(TestCase):
    """Test admin functionality"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.superuser = User.objects.create_superuser(
            username='superuser',
            email='super@example.com',
            password='superpass123'
        )
        
        self.blog = Blog.objects.create(
            user=self.user,
            title='Test Blog'
        )
        self.post = Post.objects.create(
            blog=self.blog,
            title='Test Post',
            content='<p>Test content</p>'
        )
        self.tag = Tag.objects.create(name='Django')
        
        self.client = Client()
    
    def test_regular_user_cannot_access_admin(self):
        """
        Test that regular users cannot access admin.
        
        PURPOSE: Verifica que los usuarios normales NO pueden acceder
        al panel de administración de Django. Deben ser redirigidos
        al login (código 302) ya que no tienen permisos de staff.
        """
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_superuser_can_access_admin(self):
        """
        Test that superusers can access admin.
        
        PURPOSE: Verifica que los superusuarios SÍ pueden acceder
        al panel de administración de Django. Deben recibir
        un código 200 (OK) ya que tienen permisos de staff.
        """
        self.client.login(username='superuser', password='superpass123')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
    
    def test_admin_blog_list(self):
        """
        Test admin blog list.
        
        PURPOSE: Verifica que la página de listado de blogs en el admin
        funciona correctamente. Debe mostrar todos los blogs y contener
        el título del blog de prueba.
        """
        self.client.login(username='superuser', password='superpass123')
        response = self.client.get('/admin/core/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Blog')
    
    def test_admin_post_list(self):
        """
        Test admin post list.
        
        PURPOSE: Verifica que la página de listado de posts en el admin
        funciona correctamente. Debe mostrar todos los posts y contener
        el título del post de prueba.
        """
        self.client.login(username='superuser', password='superpass123')
        response = self.client.get('/admin/core/post/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
    
    def test_admin_tag_list(self):
        """
        Test admin tag list.
        
        PURPOSE: Verifica que la página de listado de tags en el admin
        funciona correctamente. Debe mostrar todos los tags y contener
        el nombre del tag de prueba.
        """
        self.client.login(username='superuser', password='superpass123')
        response = self.client.get('/admin/core/tag/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django')