from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny  # 👈 Importamos AllowAny
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # 👈 Permite que cualquiera pueda registrarse

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)  # Llama a la creación del usuario
        user = User.objects.get(username=response.data['username'])  # Obtiene el usuario creado
        token, created = Token.objects.get_or_create(user=user)  # Genera el token
        return Response({'token': token.key, 'user': response.data})  # Devuelve el token y los datos
