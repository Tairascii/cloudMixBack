from rest_framework import serializers
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        form = UserCreationForm(validated_data)
        if form.is_valid():
            user = form.save()
            return user
        else:
            raise serializers.ValidationError(form.errors)