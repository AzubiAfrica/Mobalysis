from django.db import models


class ChampionsStats(models.Model):
    championid = models.IntegerField(
        db_column="championId", blank=True, null=True
    )  # Field name made lowercase.
    region = models.CharField(max_length=100, blank=True, null=True)
    tier = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    fgm = models.CharField(
        db_column="fgm", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    winrate = models.FloatField(blank=True, null=True)
    banrate = models.FloatField(blank=True, null=True)
    pickrate = models.FloatField(blank=True, null=True)
    kills = models.FloatField(blank=True, null=True)
    deaths = models.FloatField(blank=True, null=True)
    assists = models.FloatField(blank=True, null=True)
    pentakills = models.FloatField(blank=True, null=True)
    games_played = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "champions_stats"
