from api.models.regions import regions
from django.db import models
from api.models.runes import Rune
from api.models.runes_path import RunePath
from api.models.matches import matches
from api.models.champions import champions
from django.core.validators import MaxValueValidator
from api.models.summoner import summoner


class rune_match_performance(models.Model):

    gameId = models.ForeignKey(
        matches,
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT
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

    runeId = models.ForeignKey(
        Rune,
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
    )

    runepathId = models.ForeignKey(
        RunePath,
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
    )

    platformId = models.ForeignKey(
        regions,
        to_field="platformId",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
    )

    summonerId = models.ForeignKey(
        summoner,
        to_field="name",
        db_index=True,
        null=True,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
    )

    summoner_level = models.PositiveIntegerField(
        db_index=True,
        null=False,
        blank=False,
    )

    champLevel = models.PositiveIntegerField(
        db_index=True,
        null=False,
        blank=True,
    )

    win = models.PositiveSmallIntegerField(
        db_index=True,
        null=False,
        blank=False,
        validators=[MaxValueValidator(1)]
    )

    gameMode = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    tier_id = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    summoner_id = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default=''
    )
 
    def __str__(self):
        return f'''{self.championId} - {self.gameId}'''
