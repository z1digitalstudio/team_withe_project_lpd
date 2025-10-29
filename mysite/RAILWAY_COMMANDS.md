# 🚀 Comandos para Despliegue en Railway

## 📋 Preparación Previa

### 1. Instalar Railway CLI
```bash
# macOS
brew install railway

# O con npm
npm install -g @railway/cli
```

### 2. Login en Railway
```bash
railway login
```

## 🚀 Despliegue Inicial

### 1. Inicializar proyecto en Railway
```bash
# En el directorio del proyecto
cd /Users/luisparadela/Desktop/dev/1710-cms/mysite

# Inicializar Railway
railway init
```

### 2. Conectar con GitHub (opcional)
```bash
# Conectar repositorio
railway connect

# O hacer push directo
railway up
```

### 3. Configurar variables de entorno
```bash
# Configurar variables una por una
railway variables set SECRET_KEY="tu-secret-key-muy-larga"
railway variables set DEBUG=False
railway variables set ALLOWED_HOSTS="tu-proyecto.railway.app"

# O configurar desde archivo .env
railway variables set --file .env
```

## 🔧 Comandos de Gestión

### Variables de Entorno
```bash
# Ver todas las variables
railway variables

# Agregar variable
railway variables set NOMBRE_VARIABLE="valor"

# Eliminar variable
railway variables delete NOMBRE_VARIABLE

# Ver logs de variables
railway variables logs
```

### Base de Datos
```bash
# Conectar a la base de datos
railway connect

# Ejecutar migraciones
railway run python manage.py migrate

# Crear superusuario
railway run python manage.py createsuperuser

# Shell de Django
railway run python manage.py shell
```

### Logs y Monitoreo
```bash
# Ver logs en tiempo real
railway logs

# Ver logs de un servicio específico
railway logs --service web

# Ver métricas
railway status
```

## 🚀 Comandos de Despliegue

### Despliegue Manual
```bash
# Hacer deploy
railway up

# Deploy con mensaje
railway up --message "Descripción del cambio"

# Deploy desde rama específica
railway up --branch main
```

### Rollback
```bash
# Ver historial de deploys
railway status

# Hacer rollback a versión anterior
railway rollback

# Rollback a versión específica
railway rollback --version VERSION_ID
```

## 🔄 Comandos de Desarrollo

### Desarrollo Local con Railway
```bash
# Ejecutar comando en Railway
railway run python manage.py migrate

# Ejecutar shell
railway run python manage.py shell

# Ejecutar tests
railway run python manage.py test
```

### Backup y Restore
```bash
# Backup de base de datos
railway run pg_dump -U postgres $DATABASE_URL > backup.sql

# Restore de base de datos
railway run psql $DATABASE_URL < backup.sql
```

## 📊 Comandos de Información

### Información del Proyecto
```bash
# Ver información del proyecto
railway status

# Ver URL del proyecto
railway domain

# Ver variables de entorno
railway variables

# Ver servicios activos
railway service
```

### Logs y Debugging
```bash
# Ver logs recientes
railway logs --tail 100

# Filtrar logs por nivel
railway logs --level error

# Ver logs de un timeframe específico
railway logs --since 1h
```

## 🛠️ Comandos de Mantenimiento

### Reiniciar Servicios
```bash
# Reiniciar todos los servicios
railway restart

# Reiniciar servicio específico
railway restart --service web
```

### Limpieza
```bash
# Limpiar logs antiguos
railway logs --clean

# Ver uso de recursos
railway usage
```

## 🚨 Comandos de Emergencia

### Si algo sale mal
```bash
# Ver estado completo
railway status --verbose

# Ver logs de error
railway logs --level error

# Reiniciar todo
railway restart --all

# Rollback de emergencia
railway rollback --force
```

## 📝 Checklist de Despliegue

### Antes del Deploy
- [ ] Variables de entorno configuradas
- [ ] `DEBUG=False` en producción
- [ ] `SECRET_KEY` segura
- [ ] `ALLOWED_HOSTS` configurado
- [ ] Migraciones ejecutadas

### Después del Deploy
- [ ] Verificar que la app responde
- [ ] Probar endpoints principales
- [ ] Verificar logs sin errores
- [ ] Probar autenticación
- [ ] Verificar base de datos

## 🔗 URLs Importantes

- **Panel de Railway:** https://railway.app/dashboard
- **Documentación:** https://docs.railway.app/
- **Tu App:** `https://tu-proyecto.railway.app`

## 💡 Tips y Trucos

### Variables de Entorno Comunes
```bash
# Para producción
railway variables set DEBUG=False
railway variables set SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
railway variables set ALLOWED_HOSTS="tu-dominio.railway.app"
```

### Comandos Útiles
```bash
# Ver configuración actual
railway status --json

# Exportar variables a archivo
railway variables --json > railway-vars.json

# Importar variables desde archivo
railway variables set --file railway-vars.json
```

## 🆘 Solución de Problemas

### Error de Conexión a DB
```bash
# Verificar variables de DB
railway variables | grep DATABASE

# Probar conexión
railway run python manage.py dbshell
```

### Error 500
```bash
# Ver logs detallados
railway logs --level error

# Verificar variables
railway variables
```

### Error de Migraciones
```bash
# Ejecutar migraciones manualmente
railway run python manage.py migrate --run-syncdb
```

---

**¡Recuerda siempre hacer backup antes de cambios importantes!** 🚨
