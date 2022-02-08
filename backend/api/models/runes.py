from django.db import models
from api.models.runes_path import RunePath


class Rune(models.Model):
    id = models.CharField(
        max_length=200, primary_key=True, null=False, blank=False, db_index=True
    )

    pathid = models.ForeignKey(
        RunePath,
        db_index=True,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
    )

    name = models.CharField(max_length=200, null=False, blank=False, db_index=True)

    icon = models.CharField(max_length=200, null=False, blank=False, default="")

    shortDesc = models.TextField(null=False, blank=False, default="")

    longDesc = models.TextField(null=False, blank=False, default="")

    key = models.CharField(
        max_length=200, null=False, blank=False, db_index=True, default=""
    )

    slot = models.SmallIntegerField(null=True, blank=True, db_index=True)

    version = models.CharField(max_length=20, null=True, blank=False, db_index=True)

    def __str__(self):
        return f"""{self.id} - {self.name}"""
