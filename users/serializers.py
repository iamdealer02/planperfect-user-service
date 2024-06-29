from rest_framework import serializers
from .models import Users
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = Users.objects.create_user(
            email = validated_data['email'],
            fname = validated_data['fname'],
            lname = validated_data['lname'],
            password = validated_data['password']
        
        )
        return user
    

class LoginSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if user.is_active:
                    return {'user': user}
                else:
                    raise serializers.ValidationError('Account is disabled')
            else:
                raise serializers.ValidationError('Invalid credentials')
        else:
            raise serializers.ValidationError('Must include "email" and "password"')
  
