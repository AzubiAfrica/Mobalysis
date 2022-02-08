from django.db import models

class ChampionSpell(models.Model):
    champion_id = models.CharField(max_length=100, null=True, blank=True)
    champion_key = models.CharField(max_length=100, null=True, blank=True)
    champion_name = models.CharField(max_length=100, null=True, blank=True)
    spell_id = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = "champion_spells"