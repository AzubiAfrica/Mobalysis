from django.db import models


class RunePath(models.Model):

    id = models.PositiveIntegerField(
        primary_key=True, null=False, blank=False, db_index=True
    )

    key = models.CharField(
        max_length=200, null=False, blank=False, db_index=True, default=""
    )

    name = models.CharField(max_length=200, null=False, blank=False, db_index=True)

    icon = models.CharField(max_length=200, null=False, blank=False, default="")

    description = models.TextField(max_length=200, null=True, blank=True, default="")

    def __str__(self):
        return f"""{self.key} - {self.name}"""
