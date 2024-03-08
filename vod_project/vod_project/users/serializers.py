from rest_framework import serializers
from .models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'name', 'phone', 'birth_date', 'gender', 'address']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data.get('name', ''),
            phone=validated_data.get('phone', ''),
            birth_date=validated_data.get('birth_date', ''),
            gender=validated_data.get('gender', ''),
            address=validated_data.get('address', ''),
            is_email_verified=False
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

