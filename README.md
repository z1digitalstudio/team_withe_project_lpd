📰 1710-CMS – Blog CMS con Django

Un CMS (Content Management System) desarrollado con Django, que permite a los usuarios crear y administrar su propio blog personal.
Cada usuario puede registrarse, crear publicaciones con un editor enriquecido (TinyMCE), añadir imágenes, etiquetas, y gestionar todo su contenido desde el panel de administración o mediante una API REST.

🚀 Estado del Proyecto

✅ Completado

Este proyecto forma parte del Proyecto 1: Blog CMS con Django, cuyo objetivo fue aprender a configurar, desarrollar y documentar un CMS completo utilizando el ecosistema Django.

🧱 Arquitectura del Sistema
🔹 Modelos de Datos
User (Django built-in)
 └── Blog (1:1 con User)
      └── Post (N:1 con Blog)
           └── Tag (M:N con Post)

🔹 Funcionalidades Principales

Registro y autenticación de usuarios

Creación y gestión de blogs personales

Editor de texto enriquecido (TinyMCE)

Sistema de etiquetas reutilizables

Subida y gestión de imágenes

Exportación e importación de contenido (CSV, JSON, XLS)

API REST funcional para consumo externo

Panel de administración personalizado por usuario

⚙️ Instalación y Ejecución Local
1️⃣ Clonar el repositorio
git clone https://github.com/luisparadela-z1/1710-cms.git
cd 1710-cms/mysite

2️⃣ Activar el entorno virtual
source ../venv/bin/activate

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Aplicar migraciones
python manage.py migrate

5️⃣ Crear superusuario
python manage.py createsuperuser

6️⃣ Ejecutar el servidor
python manage.py runserver

7️⃣ Acceder desde el navegador

Panel Admin: http://127.0.0.1:8000/admin/

Blog público: http://127.0.0.1:8000/blog/

🗂️ Estructura del Proyecto
1710-cms/
│
├── mysite/
│   ├── core/
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── templates/core/
│   │       ├── post_list.html
│   │       └── post_detail.html
│   │
│   ├── mysite/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   │
│   ├── manage.py
│
├── venv/
└── README.md

📦 Dependencias Principales

Archivo requirements.txt:

Django>=5.2
django-tinymce>=4.0
django-import-export>=4.0
django-rest-framework>=3.15
Pillow>=10.0


Instalación:

pip install -r requirements.txt

🧭 Funcionalidades Implementadas
Funcionalidad	Estado	Descripción
Registro/Login de usuarios	✅	Sistema de autenticación integrado
Blog personal por usuario	✅	Cada usuario tiene su propio blog
Creación y edición de posts	✅	Editor TinyMCE desde el admin
Etiquetas reutilizables	✅	Relación ManyToMany con Post
Subida de imágenes	✅	Campo cover en los posts
Filtros y búsqueda en admin	✅	Personalización avanzada de admin
API REST funcional	✅	Endpoints para Blog, Post y Tag
Exportación/Importación de datos	✅	Integrado con django-import-export
Control de visibilidad por usuario	✅	Cada usuario ve solo su contenido
Frontend básico con templates	✅	Listado y detalle de posts publicados
🔌 Endpoints Principales (API REST)
Endpoint	Método	Descripción
/api/blogs/	GET / POST	Listar o crear blogs
/api/posts/	GET / POST	Listar o crear posts
/api/tags/	GET / POST	Listar o crear etiquetas
/api/posts/<id>/	GET / PUT / DELETE	Ver, editar o eliminar un post

La API utiliza Django REST Framework con autenticación básica.

🧠 Enfoque Formativo y Aprendizaje con IA

Este proyecto fue desarrollado con un enfoque educativo, utilizando la IA como copiloto de aprendizaje.
Se fomentó:

Comprensión profunda del ecosistema Django

Escritura manual de todo el código

Uso de IA para consultas, depuración y buenas prácticas

🧰 Tecnologías y Librerías

Django – Framework principal

Django REST Framework – API REST

django-tinymce – Editor HTML enriquecido

django-import-export – Exportación e importación de datos

Pillow – Manejo de imágenes

SQLite – Base de datos de desarrollo

Comandos de uso diario:

 # Levantar el servidor
docker-compose up

# Levantar en segundo plano
docker-compose up -d

# Parar el servidor
docker-compose down

# Ver logs
docker-compose logs

# Ejecutar comandos Django
docker-compose run web python manage.py [comando]

URLs disponibles:
http://127.0.0.1:8000/ - API Root
http://127.0.0.1:8000/admin/ - Panel de administración
http://127.0.0.1:8000/api/ - API REST
http://127.0.0.1:8000/swagger/ - Documentación de la API
Servicios incluidos:
Django (Puerto 8000)
PostgreSQL (Puerto 5432)

📘 Objetivos de Aprendizaje Alcanzados

✅ Configuración completa de proyectos Django
✅ Diseño de modelos y relaciones entre entidades
✅ Personalización avanzada del panel admin
✅ Implementación de API REST con DRF
✅ Gestión de dependencias y entorno virtual
✅ Buenas prácticas de código y estructura
✅ Documentación y pruebas básicas

💡 Autor

👤 Luis Paradela
📦 GitHub: luisparadela-z1

🏁 Conclusión

El proyecto 1710-CMS cumple con todos los objetivos planteados del Proyecto 1: Blog CMS con Django, sirviendo como base sólida para futuros desarrollos, incluyendo dashboards personalizados, autenticación avanzada y despliegue en la nube.
