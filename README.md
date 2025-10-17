# 📰 1710-CMS (Django Blog CMS)

Este proyecto es un **CMS (Content Management System)** creado con Django.  
Permite a cada usuario tener su propio blog, crear publicaciones con un editor de texto enriquecido (TinyMCE), subir imágenes, asignar etiquetas y gestionarlas desde el panel de administración.

---

## 🚀 Estado actual del proyecto

### ✅ **Configuración completada**
- Proyecto base Django (`mysite`)
- Aplicación principal (`core`)
- Entorno virtual configurado
- Módulos instalados y migraciones aplicadas
- Superusuario creado y acceso al panel de administración habilitado

### ✅ **Integraciones implementadas**
- **TinyMCE** como editor de texto enriquecido para los posts
- **Django Import-Export** para importar/exportar contenido desde el panel de admin
- Configuración de **MEDIA_URL** y **MEDIA_ROOT** para subir imágenes
- Administración personalizada: cada usuario solo puede ver y editar su propio blog y posts

### ✅ **Modelos implementados**
#### `Blog`
Cada usuario tiene un blog con:
- `title`: título del blog
- `bio`: descripción o biografía
- `user`: relación OneToOne con el usuario

#### `Tag`
Sistema de etiquetas reutilizables.

#### `Post`
Modelo principal con:
- `title`, `slug`, `content`, `excerpt`, `cover`, `tags`
- Campos de control: `is_published`, `created_at`, `updated_at`, `published_at`
- Relación con `Blog`

### ✅ **Panel de administración**
- Integración de TinyMCE para edición de texto
- Filtros, búsqueda y listado personalizados
- Usuarios no superusuarios solo pueden ver su propio contenido

### ✅ **Frontend actual**
- `/blog/` → lista todos los posts publicados
- `/blog/<slug>/` → muestra el contenido completo de un post
- Templates:  
  - `post_list.html`
  - `post_detail.html`

---

## ⚙️ **Instalación y ejecución local**

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/luisparadela-z1/1710-cms.git
cd 1710-cms/mysite

2️⃣ Activar el entorno virtual
source ../venv/bin/activate

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Aplicar migraciones
python manage.py migrate

5️⃣ Crear superusuario (si no lo has hecho)
python manage.py createsuperuser

6️⃣ Ejecutar el servidor de desarrollo
python manage.py runserver

7️⃣ Accede desde el navegador

Admin: http://127.0.0.1:8000/admin/

Blog público: http://127.0.0.1:8000/blog/

📦 Estructura del proyecto
1710-cms/
│
├── mysite/
│   ├── mysite/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   │
│   ├── core/
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── templates/
│   │       └── core/
│   │           ├── post_list.html
│   │           └── post_detail.html
│   │
│   ├── manage.py
│
├── venv/
│
└── README.md

📚 Dependencias principales

Archivo requirements.txt recomendado:

Django>=5.2
django-tinymce>=4.0
django-import-export>=4.0
Pillow>=10.0


Instálalas con:

pip install -r requirements.txt

🧭 Funcionalidades disponibles
Funcionalidad	Estado	Descripción
Crear Blogs por usuario	✅	Cada usuario tiene un blog propio
Crear Posts con editor	✅	Editor TinyMCE activado
Añadir etiquetas	✅	Sistema de tags reutilizables
Subir imágenes	✅	Campo cover en los posts
Filtrar y buscar en el admin	✅	Configurado en admin.py
Mostrar posts publicados	✅	Listado en /blog/
Detalle del post	✅	Vista /blog/<slug>/
Control de visibilidad por usuario	✅	Cada usuario ve solo su blog
🔮 Pendiente por implementar (Día 2 y siguientes)
🔹 Fase 2 – Mejoras del blog público

 Añadir paginación al listado de posts

 Mostrar imagen de portada (cover) en post_list.html

 Mostrar etiquetas y autor en post_detail.html

 Añadir sistema de comentarios

🔹 Fase 3 – Autenticación y dashboards

 Permitir registro y login desde el frontend

 Dashboard de usuario fuera del admin

 Perfil público (/user/<username>/)

🔹 Fase 4 – Diseño y estilo

 Crear plantilla base (base.html)

 Integrar TailwindCSS o Bootstrap

 Añadir cabecera, footer y navegación responsive

🔹 Fase 5 – API y despliegue

 Implementar API REST con Django REST Framework

 Preparar para despliegue en Render / Railway / Vercel

💡 Autor

👤 Luis Paradela
📦 GitHub: luisparadela-z1

🗓️ Próximo paso

➡️ Día 2:
Implementar comentarios, mostrar imágenes y etiquetas en el frontend, y crear una plantilla base con un diseño inicial.



