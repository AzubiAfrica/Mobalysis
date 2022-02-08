from django.db import models
import uuid


class summoner(models.Model):

    id = models.CharField(max_length=256, primary_key=True)
    accountid = models.CharField(max_length=256)
    puuid = models.CharField(max_length=256)
    name = models.CharField(max_length=256, unique=True)
    profileiconid = models.CharField(max_length=256)
    revisiondate = models.CharField(max_length=256)
    summonerlevel = models.CharField(max_length=256)
    region = models.CharField(max_length=256)
    tier = models.CharField(max_length=256)

    class Meta:
        db_table = "summoners"

    def __str__(self):
        return f""" {self.id} - {self.name}"""
