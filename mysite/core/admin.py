from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Blog, Post, Tag


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    search_fields = ('title', 'user__username')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    list_display = ('title', 'blog', 'created_at', 'updated_at')
    list_filter = ('created_at', 'tags')
    search_fields = ('title', 'content')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

    def save_model(self, request, obj, form, change):
        """Asigna automáticamente el blog del usuario si no es superuser"""
        if not request.user.is_superuser:
            obj.blog = Blog.objects.filter(user=request.user).first()
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        """Filtra los posts según el usuario"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(blog__user=request.user)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
