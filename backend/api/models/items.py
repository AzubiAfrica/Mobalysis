from django.db import models
from django.contrib.postgres.fields import ArrayField


class item(models.Model):
    id = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        db_index=True,
        primary_key=True,
        default="empty",
    )

    name = models.CharField(
        max_length=200, null=False, blank=False, db_index=True, default="empty"
    )

    description = models.TextField(
        max_length=200, null=False, blank=False, db_index=True, default="empty"
    )

    requiredChampion = models.CharField(
        max_length=200, blank=True, db_index=True, default=""
    )

    requiredAlly = models.CharField(
        max_length=200, blank=True, db_index=True, default=""
    )

    plaintext = models.CharField(
        max_length=200, null=False, blank=False, default="empty"
    )

    consumed = models.BooleanField(default=False, null=False, blank=False)

    inStore = models.BooleanField(default=True, null=False, blank=True)

    hideFromAll = models.BooleanField(default=False, null=False, blank=True)

    consumeOnFull = models.BooleanField(default=False, null=False, blank=False)

    stacks = models.IntegerField(default=1, null=False, blank=True)

    specialRecipe = models.IntegerField(default=1, null=False, blank=True)

    depth = models.IntegerField(default=1, null=False, blank=True)

    image = models.JSONField(null=False, blank=False, default=dict)

    gold = models.JSONField(null=False, blank=True, db_index=True, default=dict)

    tags = ArrayField(
        models.CharField(
            max_length=200,
            blank=True,
        ),
        default=list,
    )

    into = ArrayField(
        models.CharField(
            max_length=200,
            blank=True,
        ),
        default=list,
    )

    frrom = ArrayField(
        models.CharField(
            max_length=200,
            blank=True,
        ),
        default=list,
    )

    maps = models.JSONField(null=False, blank=True, default=dict)

    stats = models.JSONField(null=False, blank=True, default=dict)

    effect = models.JSONField(null=False, blank=True, default=dict)

    rune = models.JSONField(null=False, blank=True, default=dict)

    version = models.CharField(max_length=20, null=True, blank=False, db_index=True)

    def __str__(self):
        return f"""{self.id} - {self.name}"""
