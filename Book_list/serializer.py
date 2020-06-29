from rest_framework import serializers

from .models import Books


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = [
            'id',
            'name',
            'language',
            'price',
            'amazonlink'
        ]