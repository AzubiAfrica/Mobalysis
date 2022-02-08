# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from api.models.champions import champions


class ItemsStats(models.Model):
    championid = models.ForeignKey(
        champions,
        to_field="key",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
        db_column="championId",
    )
    region = models.TextField(blank=True, null=True)
    fgm = models.TextField(blank=True, null=True)
    tier = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)
    starter_item = models.TextField(blank=True, null=True)
    early_item = models.TextField(blank=True, null=True)
    winrate = models.FloatField(blank=True, null=True)
    games_played = models.BigIntegerField(blank=True, null=True)
    pickrate = models.FloatField(blank=True, null=True)
    starter_time = models.FloatField(blank=True, null=True)
    early_time = models.FloatField(blank=True, null=True)
    core_time = models.FloatField(blank=True, null=True)
    core_items = models.TextField(blank=True, null=True)
    full_build = models.TextField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = "items_stats"
