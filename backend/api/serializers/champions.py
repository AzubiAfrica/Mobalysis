from rest_framework import serializers
from api.models.champions import champions


class ChampionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = champions
        fields = '__all__'
