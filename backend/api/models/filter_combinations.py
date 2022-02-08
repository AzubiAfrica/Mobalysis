from django.db import models

class FilterCombination(models.Model):
    filter_id = models.BigIntegerField()
    filter_value = models.TextField()

    class Meta:
        managed = False
        db_table = "filter_combinations"