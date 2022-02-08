from django.db import models
from api.models.rune_page import RunePage


class RuneStatistics(models.Model):
    rune_page_id = models.ForeignKey(
        RunePage,
        to_field="rune_page_id",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
        db_column="rune_page_id",
    )
    championId = models.TextField(null=False, blank=False)
    role = models.TextField(null=True, blank=False)
    region = models.TextField(null=True, blank=False)
    fgm = models.TextField(null=True, blank=False)
    tier = models.TextField(null=True, blank=False)
    duration = models.TextField(null=True, blank=False)
    winrate = models.FloatField(blank=False, null=False)
    pickrate = models.FloatField(blank=False, null=False)

    class Meta:
        db_table = "rune_statistics"
