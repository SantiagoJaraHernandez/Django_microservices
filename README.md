# Mi Proyecto Django

Este es un proyecto de Django que incluye autenticación por tokens con `djangorestframework`.

## 🚀 Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. Crea un entorno virtual y actívalo:
   ```sh
   python -m venv myenv
   source myenv/bin/activate  # En macOS/Linux
   myenv\Scripts\activate     # En Windows
   ```

3. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

4. Ejecuta las migraciones:
   ```sh
   python manage.py migrate
   ```

5. Inicia el servidor:
   ```sh
   python manage.py runserver
   ```

## 🔑 Autenticación

Este proyecto usa **autenticación por tokens** con `djangorestframework`. Para obtener un token de usuario, usa:

```sh
curl -X POST http://localhost:8000/api/token/ -d "username=admin&password=admin"
```

Luego, usa el token en las solicitudes:

```sh
curl -H "Authorization: Token tu_token_aqui" http://localhost:8000/api/orders/
```
