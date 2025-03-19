from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]  # 👈 Se usa como atributo de clase
    permission_classes = [IsAuthenticated]  # 👈 Se usa como atributo de clase
