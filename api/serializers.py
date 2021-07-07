from rest_framework import serializers
from .models import ErrorCodeModel


class ErrorCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorCodeModel
        fields = '__all__'
