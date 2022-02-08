from django.db import models
from api.models.champions import champions


class SkillOrders(models.Model):

    championid = models.CharField(
        db_column="championid", max_length=100, blank=True, null=True
    )
    tier = models.TextField(
        max_length=100,
        null=True,
        blank=True,
    )

    role = models.TextField(
        max_length=100,
        null=True,
        blank=True,
    )


    region = models.TextField(
        max_length=100,
        null=True,
        blank=True,
    )

    fgm = models.TextField(
        max_length=100,
        null=True,
        blank=True,
    )

    winrate = models.FloatField(blank=True, null=True)

    pickrate = models.FloatField(blank=True, null=True)

    spell_1_level_1 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_1_level_2 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )
    spell_1_level_3 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_1_level_4 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_1_level_5 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_1_level_6 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_2_level_1 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_2_level_2 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )
    spell_2_level_3 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_2_level_4 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_2_level_5 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_2_level_6 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_3_level_1 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_3_level_2 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )
    spell_3_level_3 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_3_level_4 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_3_level_5 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_3_level_6 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_4_level_1 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_4_level_2 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )
    spell_4_level_3 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_4_level_4 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_4_level_5 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )

    spell_4_level_6 = models.TextField(
        max_length=4,
        null=True,
        blank=True,
    )
    games_played = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.championid}" 
