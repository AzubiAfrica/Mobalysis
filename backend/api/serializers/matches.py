from rest_framework import serializers
from api.models.matches import matches


class MatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = matches
        fields = '__all__'
