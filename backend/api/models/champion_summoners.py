from django.db import models
from api.models.champions import champions
from api.models.summoner import summoner


class ChampionSummoners(models.Model):
    summonername = models.TextField(blank=False)

    championid = models.ForeignKey(
        champions,
        to_field="key",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        unique=False,
        db_column="championid",
    )
    platformid = models.TextField(blank=False)

    duration = models.TextField(db_column="gameduration", null=True)

    fgm = models.TextField(db_column="gamemode", null=True)

    tier = models.TextField(
        blank=False,
    )
    role = models.TextField(db_column="final_role", null=True)
    winrate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    rank = models.IntegerField(blank=True, null=True)

    games_played = models.IntegerField(
        blank=False, null=False, db_column="games_played", default=int(0)
    )

    class Meta:
        db_table = "summoner_champions"
