from django.db import models
from api.models.champions import champions
from api.models.matches import matches
from django.core.validators import MaxValueValidator
from api.models.ranks import rank
from api.models.summoner import summoner
from api.models.tier import tier


class champion_match_performance(models.Model):

    gameId = models.ForeignKey(
        matches, db_index=True, null=False, blank=False, on_delete=models.PROTECT
    )

    championId = models.ForeignKey(
        champions,
        to_field="key",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
    )

    tier = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    summonerId = models.ForeignKey(
        summoner,
        db_index=True,
        null=True,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
    )

    champLevel = models.PositiveIntegerField(
        db_index=True,
        null=False,
        blank=False,
    )

    win = models.PositiveSmallIntegerField(
        db_index=True, null=False, blank=False, validators=[MaxValueValidator(1)]
    )

    role = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    lane = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    kills = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
    )

    deaths = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
    )

    assists = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
    )

    pentakills = models.FloatField(
        null=False,
        blank=False,
    )

    platformId = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    gameMode = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"""{self.championId} - {self.gameId}"""
