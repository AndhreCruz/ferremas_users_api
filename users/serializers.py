from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Role, User, Client

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
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