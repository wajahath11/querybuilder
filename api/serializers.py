from rest_framework import serializers
from .models import Bankdata


class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bankdata
        fields = '__all__'