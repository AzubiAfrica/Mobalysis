from django.http import JsonResponse

import boto3
import os

from .regions import regions


def get_filters(request):
    from api.models.champions import champions

    filter_args = dict()

    if request.GET.get("region"):
        fields = regions
        filter_args.update(region=fields.get(request.GET.get("region")))
    else:
        filter_args.update(region="All")

    if request.GET.get("tier"):
        fields = dict(
            [
                ("1", "All"),
                ("2", "CHALLENGER"),
                ("3", "GRANDMASTER"),
                ("4", "MASTER"),
                ("5", "DIAMOND"),
                ("6", "PLATINUM"),
                ("7", "GOLD"),
                ("8", "SILVER"),
                ("9", "BRONZE"),
                ("10", "IRON"),
            ]
        )
        filter_args.update(tier=fields.get(request.GET.get("tier")))
    else:
        filter_args.update(tier="All")

    if request.GET.get("role"):
        fields = dict(
            [
                ("1", "All"),
                ("2", "top laner"),
                ("3", "mid laner"),
                ("4", "jungler"),
                ("5", "Support"),
                ("6", "Bot"),
            ]
        )
        filter_args.update(role=fields.get(request.GET.get("role")))
    else:
        filter_args.update(role="All")

    if request.GET.get("champion"):
        champion_id = request.GET.get("champion")
        key = "All"
        if champion_id != "All":
            champion = champions.objects.get(id__iexact=champion_id)
            key = champion.key
            filter_args.update(championid=key)


    return filter_args
