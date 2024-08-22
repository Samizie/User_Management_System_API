from rest_framework import serializers
from .models import UserMan

class UserManSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMan
        fields = '__all__'
        #fields = ['id', 'name']