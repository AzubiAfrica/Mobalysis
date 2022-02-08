from django.db import models
from api.models.champions import champions


class champion_match_bans(models.Model):

    gameId = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        db_index=True
    )

    championId = models.ForeignKey(
        champions,
        to_field="key",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False
    )

    def __str__(self):
        return f''' {self.gameId} - {self.championId}'''
