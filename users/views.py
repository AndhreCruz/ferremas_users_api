from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Role, User, Client, Address, Phone
from .serializers import RoleSerializer, UserSerializer, ClientSerializer, AddressSerializer, PhoneSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer  
    
@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    try:
        user = User.objects.get(user_email=email, user_password=password)
        return Response({
            'mensaje': 'Login exitoso (User)',
            'user_id': user.user_id,
            'email': user.user_email,
            'role': user.role.role_name,
        }, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
def login_client(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    try:
        client = Client.objects.get(client_email=email, client_password=password)
        return Response({
            'mensaje': 'Login exitoso (Client)',
            'client_id': client.client_id,
            'email': client.client_email,
        }, status=status.HTTP_200_OK)
    except Client.DoesNotExist:
        return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)