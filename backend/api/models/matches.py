from django.db import models


class matches(models.Model):

    gameId = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True,
        db_index=True,
        primary_key=True
    )

    platformId = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    gameCreation = models.PositiveBigIntegerField(
        db_index=True,
        null=False,
        blank=False,
    )

    gameDuration = models.PositiveBigIntegerField(
        db_index=True,
        null=False,
        blank=False,
    )
        
    queueId = models.PositiveIntegerField(
        db_index=True,
        null=False,
        blank=False,
    )

    mapId = models.PositiveIntegerField(
        db_index=True,
        null=False,
        blank=False,
    )

    seasonId = models.PositiveIntegerField(
        db_index=True,
        null=False,
        blank=False,
    )

    gameVersion = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    gameMode = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    gameType = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.gameId