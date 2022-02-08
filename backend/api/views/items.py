from django.http import JsonResponse
from django.shortcuts import render
from .assets import current_version, base_url


def item_index(request):
    from api.models.items import item

    items = item.objects.all().values()
    data = list()
    for item in items:
        data.append(item)
    return JsonResponse({"items": data})


def get_item_build_pick_rate(item_build_stats):
    return item_build_stats.get("pickrate")


def get_item_build_win_rate(item_build_stats):
    return item_build_stats.get("winrate")


def get_item(item_id, item_properties):
    for item_property in item_properties:
        if str(item_property.get("id")) == item_id:
            image = item_property.get("image").get("full")
            image_url = f"{base_url}/dragontail-{current_version}/{current_version}/img/item/{image}"
            return dict(
                [
                    ("id", item_id),
                    ("name", item_property.get("name")),
                    ("description", item_property.get("plaintext")),
                    ("longDesc", item_property.get("description")),
                    ("image", image_url),
                ]
            )


def get_item_build_starter_items(item_build_stats, item_properties):
    items = list()
    item_time = item_build_stats.get("starter_time")
    item_category_list = eval(item_build_stats.get("starter_item"))
    for item_id in item_category_list:
        item = get_item(item_id, item_properties)
        item.update([("time", item_time)])
        items.append(item)
    return items


def get_item_build_early_items(item_build_stats, item_properties):
    items = list()
    item_time = item_build_stats.get("early_time")
    item_category_list = eval(item_build_stats.get("early_item"))
    for item_id in item_category_list:
        item = get_item(item_id, item_properties)
        item.update([("time", item_time)])
        items.append(item)
    return items


def get_item_build_core_items(item_build_stats, item_properties):
    items = list()
    item_time = item_build_stats.get("core_time")
    item_category_list = eval(item_build_stats.get("core_items"))
    for item_id in item_category_list:
        item = get_item(item_id, item_properties)
        item.update([("time", item_time)])
        items.append(item)
    return items


def get_item_build_full_build(item_build_stats, item_properties):
    items = list()
    item_category_list = eval(item_build_stats.get("full_build"))
    for item_id in item_category_list:
        item = get_item(item_id, item_properties)
        items.append(item)
    return items


def get_item_properties(item_build_stats):
    from api.models import item

    item_build = item_build_stats
    starter_items = eval(item_build.get("starter_item"))
    early_items = eval(item_build.get("early_item"))
    core_items = eval(item_build.get("core_items"))
    full_build = eval(item_build.get("full_build"))
    item_list = list(set([*starter_items, *early_items, *core_items, *full_build]))
    items = item.objects.filter(id__in=item_list).values(
        "id", "name", "plaintext", "description", "image"
    )
    return items


def get_item_build_stats(request):
    from api.models import ItemsStats
    from django.db.models import F, ExpressionWrapper, DecimalField

    filter_args = get_filters(request)
    item_build_stats = (
        ItemsStats.objects.filter(**filter_args)
        .annotate(
            games_won=ExpressionWrapper(
                F("games_played") * F("winrate"), output_field=DecimalField()
            )
        )
        .order_by("-games_won")[:1]
        .values()
    )
    return item_build_stats


def get_best_item_build(request):
    build = dict()
    item_build_stats = get_item_build_stats(request)[0]
    item_properties = get_item_properties(item_build_stats)
    build.update(
        [
            ("win_rate", get_item_build_win_rate(item_build_stats)),
            ("pick_rate", get_item_build_pick_rate(item_build_stats)),
            (
                "starter_items",
                get_item_build_starter_items(item_build_stats, item_properties),
            ),
            (
                "early_items",
                get_item_build_early_items(item_build_stats, item_properties),
            ),
            (
                "core_items",
                get_item_build_core_items(item_build_stats, item_properties),
            ),
            (
                "full_build",
                get_item_build_full_build(item_build_stats, item_properties),
            ),
        ]
    )
    return JsonResponse({"data": build})


def get_filters(request):
    from api.models.champions import champions
    from .regions import regions

    filter_args = dict()

    if request.GET.get("region"):
        fields = regions
        filter_args.update(region=fields.get(request.GET.get("region")))
    else:
        filter_args.update(region="All")

    if request.GET.get("fgm"):
        fields = dict(
            [
                ("1", "All"),
                ("2", "ARAM"),
                ("3", "URF"),
                ("4", "CLASSIC"),
            ]
        )
        filter_args.update(fgm=fields.get(request.GET.get("fgm")))
    else:
        filter_args.update(fgm="All")

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
                ("6", "Ad carry"),
            ]
        )
        filter_args.update(role=fields.get(request.GET.get("role")))
    else:
        filter_args.update(role="All")

    if request.GET.get("champion"):
        champion_id = request.GET.get("champion")
        filter_args.update(championid__id=champion_id)

    return filter_args
