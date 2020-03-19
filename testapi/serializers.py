from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    hoten = serializers.CharField(max_length=30)
    tuoi = serializers.IntegerField(default=10)
    gioitinh = serializers.CharField(max_length=5)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)