from django.db import transaction
from rest_framework import serializers

from .models import User


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        with transaction.atomic():
            # create_user() method hashes the password
            user = User.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password'],)

            return user
