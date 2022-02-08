from django.db import models


class RoleStats(models.Model):
    role = models.TextField(blank=True, null=True)
    championid = models.TextField(
        db_column="championId", blank=True, null=True
    )  # Field name made lowercase.
    region = models.TextField(blank=True, null=True)
    tier = models.TextField(blank=True, null=True)
    fgm = models.TextField(blank=True, null=True)
    winrate = models.FloatField(blank=True, null=True)
    pickrate = models.FloatField(blank=True, null=True)
    games_played = models.BigIntegerField(blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = "role_stats"
