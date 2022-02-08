from django.db import models
from api.models.items import item


class item_property(models.Model):
    itemId = models.ForeignKey(
        item,
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
    )

    attribute_name = models.CharField(
        max_length = 200,
        null=False,
        blank=False,
    )

    attribute_value = models.JSONField(
        null=False,
        blank=True,
        default=dict
    )

    def __str__(self):
        return f'''{self.itemId}'''