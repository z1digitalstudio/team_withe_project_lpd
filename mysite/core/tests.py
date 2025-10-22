from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Blog, Post, Tag

class BlogModelTest(TestCase):
    """Test basic Blog model functionality"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_blog_creation(self):
        """Test that a blog can be created"""
        blog = Blog.objects.create(
            user=self.user,
            title='Test Blog',
            bio='This is a test blog'
        )
        self.assertEqual(blog.title, 'Test Blog')
        self.assertEqual(blog.user, self.user)
        self.assertEqual(blog.bio, 'This is a test blog')
    
    def test_blog_str_representation(self):
        """Test the string representation of Blog"""
        blog = Blog.objects.create(
            user=self.user,
            title='Test Blog'
        )
        expected = f"Test Blog ({self.user.username})"
        self.assertEqual(str(blog), expected)

class TagModelTest(TestCase):
    """Test basic Tag model functionality"""
    
    def test_tag_creation(self):
        """Test that a tag can be created"""
        tag = Tag.objects.create(name='Django')
        self.assertEqual(tag.name, 'Django')
    
    def test_tag_str_representation(self):
        """Test the string representation of Tag"""
        tag = Tag.objects.create(name='Python')
        self.assertEqual(str(tag), 'Python')
    
    def test_tag_unique_name(self):
        """Test that tag names must be unique"""
        Tag.objects.create(name='Django')
        with self.assertRaises(Exception):
            Tag.objects.create(name='Django')

class PostModelTest(TestCase):
    """Test basic Post model functionality"""
    
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
        """Test that a post can be created"""
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
        """Test the string representation of Post"""
        post = Post.objects.create(
            blog=self.blog,
            title='Test Post',
            content='<p>Test content</p>'
        )
        self.assertEqual(str(post), 'Test Post')
    
    def test_post_slug_generation(self):
        """Test that slug is automatically generated"""
        post = Post.objects.create(
            blog=self.blog,
            title='Test Post Title',
            content='<p>Test content</p>'
        )
        self.assertEqual(post.slug, 'test-post-title')
    
    def test_post_with_tags(self):
        """Test that a post can have tags"""
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