from rest_framework import serializers
from .models import DB


class DB_Serializer(serializers.ModelSerializer):
    class Meta:
        model = DB
        fields = ['name', 'text']
