from rest_framework import serializers
from api.models.spells import Spell
from api.models.spell_stats import spells_stats


class SpellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = '__all__'

class SpellStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = spells_stats
        fields = '__all__'