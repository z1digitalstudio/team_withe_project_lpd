from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')

    # Paginación: 4 posts por página
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'core/post_list.html', {
        'page_obj': page_obj,
        'posts': page_obj,  
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'core/post_detail.html', {'post': post})
