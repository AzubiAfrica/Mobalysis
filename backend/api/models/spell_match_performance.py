from django.db import models
from api.models.spells import Spell
from api.models.matches import matches
from api.models.champions import champions
from django.core.validators import MaxValueValidator


class spell_match_performance(models.Model):

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

    spellId = models.ForeignKey(
        Spell,
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
    )

    summoner_level = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default=''
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
