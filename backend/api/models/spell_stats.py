from django.db import models


class spells_stats(models.Model):
    spells = models.CharField(max_length=100, db_column="spells", blank=True, null=True)
    championid = models.CharField(
        db_column="championId", blank=True, null=True, max_length=100
    )
    region = models.CharField(max_length=100, blank=True, null=True)
    tier = models.CharField(max_length=100, blank=True, null=True)
    fgm = models.CharField(db_column="fgm", max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    winrate = models.FloatField(blank=True, null=True)
    pickrate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "spell_stats"


class SpellStats(models.Model):
    spells = models.TextField(blank=True, null=True)
    championid = models.CharField(
        db_column="championId", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    region = models.TextField(blank=True, null=True)
    tier = models.TextField(blank=True, null=True)
    fgm = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)
    winrate = models.FloatField(blank=True, null=True)
    pickrate = models.FloatField(blank=True, null=True)
    games_played = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "spell_stats"
