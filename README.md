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
