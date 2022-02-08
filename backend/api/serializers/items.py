from rest_framework import serializers
from api.models.items import item


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'