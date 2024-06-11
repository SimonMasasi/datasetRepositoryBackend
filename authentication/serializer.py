from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', "first_name" ,"last_name",'is_staff']


    def create(self, validated_data):
        return super().create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)