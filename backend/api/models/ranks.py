from django.db import models


class rank(models.Model):
    tierRank= models.CharField(
        max_length=100, null=False, blank=False, unique=True, primary_key=True
    )

    def __str__(self):
        return f"""{self.tierRank}"""
