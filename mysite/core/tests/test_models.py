from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from ..models import Blog, Post, Tag

class BlogModelTest(TestCase):
    """Test Blog model functionality"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_blog_creation(self):
        """
        Test that a blog can be created.
        
        PURPOSE: Verifica que el modelo Blog se puede crear correctamente
        con todos sus campos básicos (user, title, bio). Este es el test
        fundamental para asegurar que el modelo funciona.
        """
        blog = Blog.objects.create(
            user=self.user,
            title='Test Blog',
            bio='This is a test blog'
        )
        self.assertEqual(blog.title, 'Test Blog')
        self.assertEqual(blog.user, self.user)
        self.assertEqual(blog.bio, 'This is a test blog')
    
    def test_blog_str_representation(self):
        """
        Test the string representation of Blog.
        
        PURPOSE: Verifica que el método __str__ del modelo Blog funciona
        correctamente. Esto es importante para la visualización en el admin
        y para debugging. El formato debe ser "Título (username)".
        """
        blog = Blog.objects.create(
            user=self.user,
            title='Test Blog'
        )
        expected = f"Test Blog ({self.user.username})"
        self.assertEqual(str(blog), expected)

class TagModelTest(TestCase):
    """Test Tag model functionality"""
    
    def test_tag_creation(self):
        """
        Test that a tag can be created.
        
        PURPOSE: Verifica que el modelo Tag se puede crear correctamente
        con su campo name. Los tags son elementos simples pero importantes
        para categorizar posts.
        """
        tag = Tag.objects.create(name='Django')
        self.assertEqual(tag.name, 'Django')
    
    def test_tag_str_representation(self):
        """
        Test the string representation of Tag.
        
        PURPOSE: Verifica que el método __str__ del modelo Tag funciona
        correctamente. Para los tags, el string representation debe ser
        simplemente el nombre del tag.
        """
        tag = Tag.objects.create(name='Python')
        self.assertEqual(str(tag), 'Python')
    
    def test_tag_unique_name(self):
        """
        Test that tag names must be unique.
        
        PURPOSE: Verifica que los nombres de los tags deben ser únicos.
        Esto evita duplicados y mantiene la consistencia en el sistema.
        Si se intenta crear un tag con un nombre que ya existe, debe fallar.
        """
        Tag.objects.create(name='Django')
        with self.assertRaises(Exception):
            Tag.objects.create(name='Django')

class PostModelTest(TestCase):
    """Test Post model functionality"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.blog = Blog.objects.create(
            user=self.user,
            title='Test Blog'
        )
    
    def test_post_creation(self):
        """
        Test that a post can be created.
        
        PURPOSE: Verifica que el modelo Post se puede crear correctamente
        con todos sus campos básicos (blog, title, content, excerpt).
        También verifica que is_published tiene el valor por defecto False.
        """
        post = Post.objects.create(
            blog=self.blog,
            title='Test Post',
            content='<p>This is test content</p>',
            excerpt='Test excerpt'
        )
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.blog, self.blog)
        self.assertFalse(post.is_published)  # Default should be False
    
    def test_post_str_representation(self):
        """
        Test the string representation of Post.
        
        PURPOSE: Verifica que el método __str__ del modelo Post funciona
        correctamente. Para los posts, el string representation debe ser
        el título del post.
        """
        post = Post.objects.create(
            blog=self.blog,
            title='Test Post',
            content='<p>Test content</p>'
        )
        self.assertEqual(str(post), 'Test Post')
    
    def test_post_slug_generation(self):
        """
        Test that slug is automatically generated.
        
        PURPOSE: Verifica que el slug se genera automáticamente a partir
        del título del post. Los slugs son importantes para URLs amigables
        y SEO. El slug debe ser la versión "slugificada" del título.
        """
        post = Post.objects.create(
            blog=self.blog,
            title='Test Post Title',
            content='<p>Test content</p>'
        )
        self.assertEqual(post.slug, 'test-post-title')
    
    def test_post_with_tags(self):
        """
        Test that a post can have tags.
        
        PURPOSE: Verifica que la relación Many-to-Many entre Post y Tag
        funciona correctamente. Un post puede tener múltiples tags y
        un tag puede estar en múltiples posts. Esto es fundamental
        para el sistema de categorización del CMS.
        """
        tag1 = Tag.objects.create(name='Django')
        tag2 = Tag.objects.create(name='Python')
        
        post = Post.objects.create(
            blog=self.blog,
            title='Test Post',
            content='<p>Test content</p>'
        )
        post.tags.add(tag1, tag2)
        
        self.assertEqual(post.tags.count(), 2)
        self.assertIn(tag1, post.tags.all())
        self.assertIn(tag2, post.tags.all())