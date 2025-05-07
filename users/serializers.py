from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Role, User, Client, Address, Phone

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class ClientSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='client.user.first_name', read_only=True)
    last_name = serializers.CharField(source='client.user.last_name', read_only=True)
    
    class Meta:
        model = Client
        fields = ['client_id', 'user', 'first_name', 'last_name']
        
class AddressSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='client.user.first_name', read_only=True)
    last_name = serializers.CharField(source='client.user.last_name', read_only=True)
    class Meta:
        model = Address
        fields = ['address_id', 'client', 'street', 'city', 'region', 'postal_code', 'address_type', 'is_primary', 'first_name', 'last_name']
        
class PhoneSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    class Meta:
        model = Phone
        fields = ['phone_id', 'client', 'phone_number', 'phone_type', 'is_primary', 'first_name', 'last_name']
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email' # This is the field used for authentication
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('User not found')
        
        # Check
        if user.password != password:
            raise serializers.ValidationError('Incorrect password')
        
        # Generate token if user is found and password is correct
        data = super().validate({
            'username': email,
            'password': password
        })
        
        # Add user information to the token response
        data['user_id'] = user.user_id
        data['email'] = user.email
        data['role'] = user.role.role_name
        
        return data