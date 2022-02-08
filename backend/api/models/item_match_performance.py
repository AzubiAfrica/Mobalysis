from django.db import models
from api.models.items import item
from api.models.matches import matches
from api.models.regions import regions
from api.models.champions import champions
from django.core.validators import MaxValueValidator
from api.models.summoner import summoner


class item_match_performance(models.Model):

    gameId = models.ForeignKey(
        matches, db_index=True, null=False, blank=False, on_delete=models.PROTECT
    )

    itemId = models.ForeignKey(
        item,
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
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

    platformId = models.ForeignKey(
        regions,
        to_field="platformId",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
    )

    summonerId = models.CharField(
        max_length=100,
        null=True,
        blank=False,
    )

    tier = models.CharField(
        max_length=100,
        null=True,
        blank=False,
    )

    win = models.PositiveSmallIntegerField(
        db_index=True, null=False, blank=False, validators=[MaxValueValidator(1)]
    )

    gameMode = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"""{self.itemId} - {self.gameId}"""
