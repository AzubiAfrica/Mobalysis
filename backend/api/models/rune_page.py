from django.db import models
from api.models.runes import Rune
from api.models.runes_path import RunePath


class RunePage(models.Model):
    rune_page_id = models.IntegerField(
        primary_key=True,
        null=False,
        blank=False,
        db_index=True,
        unique=True,
    )
    primary_style = models.ForeignKey(
        RunePath,
        to_field="id",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
        db_column="primary_style",
        related_name="ra_primary_style",
    )
    key_stone = models.ForeignKey(
        Rune,
        to_field="id",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
        db_column="key_stone",
        related_name="+",
    )
    primary_perk0_1 = models.ForeignKey(
        Rune,
        to_field="id",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
        db_column="primary_perk0_1",
        related_name="+",
    )
    primary_perk0_2 = models.ForeignKey(
        Rune,
        to_field="id",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
        db_column="primary_perk0_2",
        related_name="+",
    )
    primary_perk0_3 = models.ForeignKey(
        Rune,
        to_field="id",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
        db_column="primary_perk0_3",
        related_name="+",
    )
    shard1 = models.TextField(null=False, blank=False, default="")
    shard2 = models.TextField(null=False, blank=False, default="")
    shard3 = models.TextField(null=False, blank=False, default="")
    secondary_style = models.ForeignKey(
        RunePath,
        to_field="id",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
        db_column="secondary_style",
        related_name="+",
    )
    secondary_perk0_1 = models.ForeignKey(
        Rune,
        to_field="id",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
        db_column="secondary_perk0_1",
        related_name="+",
    )
    secondary_perk0_2 = models.ForeignKey(
        Rune,
        to_field="id",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
        db_column="secondary_perk0_2",
        related_name="+",
    )

    # class Meta:
    #     managed = False
    #     db_table = "rune_pages"

    def __str__(self):
        return f"""{self.rune_page_id}"""
