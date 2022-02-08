from django.db import models


class game_modes(models.Model):

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return f''' {self.id} - {self.name}'''
