# MyProject - API REST con Django y DRF

Este proyecto es una API REST desarrollada con Django y Django REST Framework (DRF). La API permite gestionar usuarios, productos y órdenes de compra.

## Tecnologías usadas
- Python 3.x
- Django 5.1.7
- Django REST Framework
- PostgreSQL

## Instalación y configuración

### 1. Clonar el repositorio
```sh
git clone https://github.com/TU-USUARIO/MyProject.git
cd MyProject
```

### 2. Crear un entorno virtual y activarlo
```sh
python -m venv myenv
source myenv/bin/activate  # En macOS/Linux
myenv\Scripts\activate     # En Windows
```

### 3. Instalar dependencias
```sh
pip install -r requirements.txt
```

### 4. Configurar la base de datos
Editar `settings.py` y asegurarse de que la configuración de la base de datos es correcta.

### 5. Aplicar migraciones y ejecutar el servidor
```sh
python manage.py migrate
python manage.py runserver
```

## Endpoints disponibles

### Autenticación
- `POST /api/auth/register/` → Registro de usuarios
- `POST /api/auth/login` → Inicio de sesion y obtencion del token 

### Productos
- `GET /api/products/` → Listar productos
- `POST /api/products/` → Crear producto
- `GET /api/products/{id}/` → Ver detalle de un producto
- `PUT /api/products/{id}/` → Actualizar producto
- `DELETE /api/products/{id}/` → Eliminar producto

### Ordenes
- `GET /api/orders/` → Listar órdenes
- `POST /api/orders/` → Crear orden
- `GET /api/orders/{id}/` → Ver detalle de una orden
- `PUT /api/orders/{id}/` → Actualizar orden
- `DELETE /api/orders/{id}/` → Eliminar orden

## Documentación interactiva con Swagger
Después de ejecutar el servidor, accede a la documentación en:
- [Swagger UI](http://127.0.0.1:8000/swagger/)
- [Redoc](http://127.0.0.1:8000/redoc/)

## Contribuciones
Si deseas contribuir, haz un **fork** del repositorio y envía un **pull request** con tus cambios.

---

📌 **Autor:** Santiago Jara Hernández  
📌 **Repositorio:** [GitHub](https://github.com/TU-USUARIO/MyProject)  

