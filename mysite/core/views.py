from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    """Muestra todos los posts publicados"""
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    print("📜 POSTS CARGADOS:", posts)
    return render(request, 'core/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'core/post_detail.html', {'post': post})
