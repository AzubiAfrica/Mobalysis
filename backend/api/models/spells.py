from django.db import models
from django.contrib.postgres.fields import ArrayField


class Spell(models.Model):

    id = models.CharField(
        max_length=200,
        # primary_key=True,
        blank=False,
        null=False,
        db_index=True,
        default="",
    )

    name = models.CharField(max_length=200, blank=False, null=False)

    description = models.TextField(blank=False, null=False, max_length=400, default="")

    tooltip = models.TextField(blank=True, null=True, max_length=200, default="")

    maxrank = models.IntegerField(blank=False, null=False, db_index=True)

    cooldown = ArrayField(models.IntegerField(blank=False, null=False), default=list)

    cooldownBurn = models.CharField(max_length=200, blank=False, null=False, default="")

    cost = ArrayField(models.IntegerField(blank=False, null=False), default=list)

    costBurn = models.CharField(max_length=200, blank=False, null=False, default="")

    datavalues = models.JSONField(null=False, blank=True, default=dict)

    effect = ArrayField(ArrayField(models.IntegerField()))
    # ArrayField(
    #     ArrayField(
    #         models.IntegerField(
    #             blank=True,
    #             null=True
    #         ),
    #         null=True,
    #     ),
    #     null=True,
    #     default=list,
    #     size=11
    # )

    effectBurn = ArrayField(
        models.CharField(max_length=200, blank=False, null=True),
        null=True,
        default=list,
    )

    vars = ArrayField(models.IntegerField(blank=True, null=False), default=list)

    key = models.CharField(
        max_length=200, primary_key=True, blank=True, null=False, default=""
    )

    summonerLevel = models.IntegerField(blank=False, null=False)

    modes = ArrayField(
        models.CharField(max_length=200, blank=True, null=False), default=list
    )

    costType = models.CharField(max_length=200, blank=True, null=False, default="")

    maxammo = models.CharField(max_length=200, blank=False, null=False, default="")

    range = ArrayField(models.IntegerField(blank=True, null=False), default=list)

    rangeBurn = models.CharField(max_length=200, blank=False, null=False)

    image = models.JSONField(null=False, blank=True, default=dict)

    resource = models.CharField(max_length=200, blank=True, null=False, default="")

    def __str__(self):
        return f"""{self.name} - {self.description}"""
