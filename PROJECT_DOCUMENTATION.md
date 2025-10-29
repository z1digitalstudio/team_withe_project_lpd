# 📚 Documentación del Proyecto - Blog CMS API

## 🎯 Descripción
Sistema de gestión de contenido (CMS) construido con Django REST Framework que permite crear y gestionar blogs, posts, usuarios y tags.

## 🏗️ Arquitectura
- **Backend:** Django 5.2.7 + Django REST Framework
- **Base de datos:** PostgreSQL 15
- **Contenedorización:** Docker + Docker Compose
- **Documentación:** Swagger/OpenAPI con drf-spectacular
- **Autenticación:** Token Authentication

## 📁 Estructura del Proyecto
```
mysite/
├── core/                    # App principal
│   ├── models.py           # Modelos (User, Blog, Post, Tag)
│   ├── views.py            # ViewSets y vistas API
│   ├── serializers.py      # Serializers para la API
│   ├── permissions.py      # Permisos personalizados
│   └── admin.py            # Configuración del admin
├── mysite/                 # Configuración del proyecto
│   ├── settings.py         # Configuración principal
│   ├── urls.py            # URLs principales
│   └── wsgi.py            # WSGI configuration
├── posts/                  # Media files
├── Dockerfile             # Configuración Docker
├── docker-compose.yml     # Orquestación de servicios
├── .env                   # Variables de entorno
└── requirements.txt       # Dependencias Python
```

## 🔧 Modelos de Datos

### User (Usuario)
- Campos: id, username, email, password
- Relación: One-to-Many con Blog

### Blog (Blog)
- Campos: id, title, description, user
- Relación: One-to-Many con Post

### Post (Post)
- Campos: id, title, content, slug, is_published, created_at, updated_at, blog, tags
- Relación: Many-to-Many con Tag

### Tag (Etiqueta)
- Campos: id, name, created_at
- Relación: Many-to-Many con Post

## 🚀 Endpoints de la API

### Autenticación
- `POST /api/users/register/` - Registro de usuarios
- `POST /api/users/login/` - Login de usuarios
- `GET /api/users/` - Lista de usuarios (solo superusuarios)

### Blogs
- `GET /api/blogs/` - Lista de blogs
- `POST /api/blogs/` - Crear blog
- `GET /api/blogs/{id}/` - Detalle de blog
- `PUT /api/blogs/{id}/` - Actualizar blog
- `DELETE /api/blogs/{id}/` - Eliminar blog

### Posts
- `GET /api/posts/` - Lista de posts
- `POST /api/posts/` - Crear post
- `GET /api/posts/{id}/` - Detalle de post
- `PUT /api/posts/{id}/` - Actualizar post
- `DELETE /api/posts/{id}/` - Eliminar post
- `GET /api/posts/published/` - Posts publicados
- `GET /api/posts/by_tag/?tag=nombre` - Posts por tag

### Tags
- `GET /api/tags/` - Lista de tags
- `POST /api/tags/` - Crear tag
- `GET /api/tags/{id}/` - Detalle de tag
- `PUT /api/tags/{id}/` - Actualizar tag
- `DELETE /api/tags/{id}/` - Eliminar tag

## 🔐 Permisos

### IsOwnerOrSuperuser
- Usuarios solo pueden ver/editar sus propios recursos
- Superusuarios pueden ver/editar todo

### IsOwnerOrSuperuserForBlog
- Usuarios solo pueden gestionar sus propios blogs
- Superusuarios pueden gestionar todos los blogs

### IsSuperuserOrReadOnly
- Cualquier usuario autenticado puede leer
- Solo superusuarios pueden crear/editar/eliminar

## 🐳 Docker

### Servicios
- **web:** Aplicación Django (puerto 8000)
- **db:** Base de datos PostgreSQL (puerto 5432)

### Variables de Entorno
- `DB_NAME`: Nombre de la base de datos
- `DB_USER`: Usuario de la base de datos
- `DB_PASSWORD`: Contraseña de la base de datos
- `SECRET_KEY`: Clave secreta de Django
- `DEBUG`: Modo debug (True/False)

## 📊 Características Técnicas

### Django REST Framework
- Paginación automática (20 elementos por página)
- Autenticación por token
- Serialización automática
- Filtros y búsquedas

### TinyMCE
- Editor de texto enriquecido
- Configuración personalizada
- Plugins: tablas, imágenes, enlaces, etc.

### Swagger/OpenAPI
- Documentación automática de la API
- Interfaz interactiva
- Autenticación integrada

## 🔧 Comandos Útiles

### Desarrollo Local
```bash
# Levantar servidor
docker-compose up

# Ejecutar migraciones
docker-compose run web python manage.py migrate

# Crear superusuario
docker-compose run web python manage.py createsuperuser

# Ver logs
docker-compose logs -f web
```

### Base de Datos
```bash
# Resetear base de datos
docker-compose down -v
docker-compose up

# Backup de base de datos
docker-compose exec db pg_dump -U postgres mysite > backup.sql
```

## 🚀 Despliegue

### Railway
- Configuración automática con Docker
- Variables de entorno en el panel de Railway
- Base de datos PostgreSQL incluida
- Dominio automático generado

### Variables de Entorno para Producción
- `DEBUG=False`
- `SECRET_KEY=clave-secreta-muy-larga`
- `ALLOWED_HOSTS=tu-dominio.railway.app`
- `DATABASE_URL=postgresql://...` (proporcionada por Railway)

## 📝 Notas de Desarrollo

### Debugging
- Usar `print()` statements para debugging
- Ver logs con `docker-compose logs -f web`
- Usar `pdb.set_trace()` para debugging interactivo

### Testing
- Tests unitarios en `core/tests/`
- Ejecutar tests: `docker-compose run web python manage.py test`

### Seguridad
- Variables sensibles en `.env`
- Archivo `.env` excluido de Docker
- Permisos granulares por recurso
- Autenticación obligatoria para la mayoría de endpoints
