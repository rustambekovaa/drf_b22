from rest_framework import serializers
from .models import Auto , CarReview, Brand
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 150)
    password = serializers.CharField(write_only=True)

    def validate(self,data):

        user = authenticate(
            username = data['username'],
            password = data['password']
        )

        if user is None:
            raise serializers.ValidationError(
                'Invalid passwor or username'
            )
            
        data['user'] = user

        return data
        



class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self,validate_data):
        user = User.objects.create_user(
            username = validate_data['username'],
            email = validate_data['email'],
            password = validate_data['password']
        )
        return user


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'



class AutoSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer()
    brand = serializers.StringRelatedField()
    

    class Meta:
        model  = Auto
        fields = '__all__'


class  CarReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CarReview
        fields = '__all__'



