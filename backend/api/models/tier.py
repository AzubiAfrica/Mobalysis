from django.db import models


class tier(models.Model):

    name = models.CharField(
        primary_key=True,
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return f''' {self.name}'''
