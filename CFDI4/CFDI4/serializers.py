from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

from Profiles.models import Profile

class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Profile
        fields = ('bio', 'avatar', 'job_title',)

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    profile = ProfileUserSerializer(many=False, read_only =False, required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
        'email', 'first_name', 'last_name',
        'profile'
        )

        extra_kwargs = {
        'first_name': {'required': True},
        'last_name': {'required': True},
        'profile':{'required':True},
        }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        if 'profile' not in attrs:
            raise serializers.ValidationError({"Profile": "no profile data "})
        return attrs

         
    
    def create(self,validated_data):
        profile = validated_data.pop('profile') if 'profile' in validated_data.keys() else dict
        
        validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        
        user.set_password(validated_data['password'])

        user.save()
        
        if 'profile' in profile.keys():
            profile = user.profile
            profile.bio = validated_data['profile']['bio']
            profile.job_title= validated_data['profile']['job_title']
            profile.save()

        
        return user

class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields used for authentication: username and password.
    It will try to authenticate the user with username/password when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},  # This will be used when the DRF browsable API is enabled
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]