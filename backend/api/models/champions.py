#from backend.api.models.champion_match_performance import champion_match_performance
from django.db import models
from django.db.models import Q, F, Sum, Avg, Value as v, Count, FloatField, IntegerField
from django.db.models.functions import Coalesce
from django.contrib.postgres.fields import JSONField

 
class ChampionManager(models.Manager):
    def with_stats(self):
        from api.models.matches import matches
        from api.models.champion_match_performance import champion_match_performance

        return self.annotate(kills=Coalesce(Avg('champion_match_performance__kills'),v(float(0)))
        , deaths=Coalesce(Avg('champion_match_performance__deaths'),v(float(0)))
        , assists=Coalesce(Avg('champion_match_performance__assists'),v(float(0)))
        , picks=Coalesce(Count('champion_match_performance'), v(float(0)), output_field=FloatField())
        , pentas=Coalesce(Sum('champion_match_performance__pentakills'), v(float(0)), output_field=FloatField())
        , wins = Coalesce(Count('champion_match_performance',filter=Q(champion_match_performance__win=1)), v(float(0)), output_field=FloatField())
        , bans=Coalesce(Count('champion_match_bans'), v(float(0)), output_field=FloatField())
        , total_matches=v(float(matches.objects.count()))
        )


class champions(models.Model):
    objects = ChampionManager()
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        db_index=True,
        default="empty"
    )

    id = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        db_index=True,
        primary_key=True,
        default="empty"
    )

    version = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        db_index=True,
        default="empty"
    )

    key = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        db_index=True,
        default="empty",
        unique=True
    )

    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default="empty"
    )

    blurb = models.TextField(
        null=False,
        blank=False,
        default="empty"
    )

    info = models.JSONField(
        null=False,
        blank=False,
        default=dict
    )

    image = models.JSONField(
        null=False,
        blank=False,
        default=dict
    )

    tags = models.JSONField(
        null=False,
        blank=False,
        default=dict
    )

    partype = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        default="empty"
    )

    stats = models.JSONField(
        null=False,
        blank=False,
        default=dict
    )

    def __str__(self):
        return f'''{self.id} - {self.version}'''

    def update(self, *args, **kwargs):
        for value, key in kwargs.items():
            try:
                setattr(self, value, key)
            except KeyError:
                pass
        self.save()
