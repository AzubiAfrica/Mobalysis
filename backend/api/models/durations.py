from django.db import models


class durations(models.Model):

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    minimumTime = models.PositiveSmallIntegerField(
        db_index=True,
        null=False,
        blank=False,
    )

    maximumTime = models.PositiveSmallIntegerField(
        db_index=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'''{self.name}'''
