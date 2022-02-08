from django.http import JsonResponse
from .assets import current_version, base_url


def rune_index(request):
    from api.models.rune_match_performance import rune_match_performance
    from api.models.matches import matches
    from api.models.runes import Rune
    from django.db.models import F, Avg, Count

    filter_args_performance = dict()
    filter_args_matches = dict()

    if request.GET.get("region"):
        filter_args_matches.update(platformId=request.GET.get("region"))

    if request.GET.get("gameMode"):
        filter_args_matches.update(gameMode__iexact=request.GET.get("gameMode"))

    if request.GET.get("gameType"):
        filter_args_matches.update(gameType__iexact=request.GET.get("gameType"))

    if request.GET.get("matchDuration"):
        matchDuration = request.GET.get("matchDuration")
        if int(matchDuration) == 1:
            filter_args_matches.update(gameDuration__gte=0)
            filter_args_matches.update(gameDuration__lte=(25 * 60))
        if int(matchDuration) == 2:
            filter_args_matches.update(gameDuration__gte=(25 * 60))
            filter_args_matches.update(gameDuration__lte=(35 * 60))
        if int(matchDuration) == 3:
            filter_args_matches.update(gameDuration__gte=(35 * 60))

    if filter_args_matches:
        qs_games = matches.objects.filter(**filter_args_matches)
    else:
        qs_games = matches.objects.all()

    if request.GET.get("rune"):
        filter_args_performance.update(runeId__name__iexact=request.GET.get("rune"))

    filter_args_performance.update(gameId__in=qs_games)

    rune_performances = (
        rune_match_performance.objects.filter(**filter_args_performance)
        .values("runeId")
        .annotate(
            winRate=Avg("win"),
            picks=Count("*"),
            name=F("runeId_id__name"),
            image=F("runeId_id__image"),
        )
    )

    runes = Rune.objects.all()
    rune_data = list()

    for rune_performance in rune_performances:
        stats = dict()
        pickRate = float(rune_performance.get("picks")) / float(qs_games.count())
        winRate = float(rune_performance.get("picks")) / float(qs_games.count())
        # winRate = round(rune_performance.get("winRate"), 2)
        image = f"""{base_url}/dragontail-{current_version}/{current_version}/img/rune/{rune_performance.get('image')['full']}"""
        stats.update(runeId=rune_performance.get("runeId"))
        stats.update(name=rune_performance.get("name"))
        stats.update(image=image)
        stats.update(gamesPlayed=rune_performance.get("picks"))
        stats.update(pickRate=round(pickRate, 2))
        stats.update(tier=request.GET.get("tier", "All Tiers"))
        stats.update(winRate=winRate)
        rune_data.append(stats)
    return JsonResponse({"runes": rune_data})


def get_primary_style(args):
    from api.models.runes import Rune
    from django.db.models import F

    primary_style_id = args.get("primary_style")
    img_base = f"{base_url}/dragontail-{current_version}/img/"
    path = (
        Rune.objects.filter(pathid=primary_style_id).annotate(
            style_name=F("pathid__name"),
            style_key=F("pathid__key"),
            style_icon=F("pathid__icon"),
            description=F("pathid__description"),
        )
    ).values()

    selected_runes = list()
    selected_runes.append(int(args.get("key_stone")))
    selected_runes.append(int(args.get("primary_perk0_1")))
    selected_runes.append(int(args.get("primary_perk0_2")))
    selected_runes.append(int(args.get("primary_perk0_3")))

    primary_style = dict(
        [("keystones", []), ("slot_1", []), ("slot_2", []), ("slot_3", [])]
    )

    for rune in path:
        selected = False
        if int(rune.get("id")) in selected_runes:
            selected = True
        rune_dict = dict(
            [
                ("selected", selected),
                ("name", rune.get("name")),
                ("icon", f'{img_base}{rune.get("icon")}'),
                ("id", rune.get("id")),
                ("key", rune.get("key")),
                ("longDesc", rune.get("longDesc")),
            ]
        )
        if int(rune.get("slot")) == 0:
            primary_style["keystones"].append(rune_dict)
        elif int(rune.get("slot")) == 1:
            primary_style["slot_1"].append(rune_dict)
        elif int(rune.get("slot")) == 2:
            primary_style["slot_2"].append(rune_dict)
        elif int(rune.get("slot")) == 3:
            primary_style["slot_3"].append(rune_dict)

    primary_style.update(
        [
            ("name", path[0].get("style_name")),
            ("key", path[0].get("style_key")),
            ("description", path[0].get("description")),
            ("id", primary_style_id),
            ("icon", f"{img_base}{path[0].get('style_icon')}"),
        ]
    )
    return primary_style


def get_sub_style(args):
    from api.models.runes import Rune
    from django.db.models import F

    sub_style_id = args.get("secondary_style")
    img_base = f"{base_url}/dragontail-{current_version}/img/"
    path = (
        Rune.objects.filter(pathid=sub_style_id).annotate(
            style_name=F("pathid__name"),
            style_key=F("pathid__key"),
            style_icon=F("pathid__icon"),
            description=F("pathid__description"),
        )
    ).values()

    selected_runes = list()
    selected_runes.append(int(args.get("secondary_perk0_1")))
    selected_runes.append(int(args.get("secondary_perk0_2")))

    sub_style = dict(
        [("keystones", []), ("slot_1", []), ("slot_2", []), ("slot_3", [])]
    )

    for rune in path:
        selected = False
        if int(rune.get("id")) in selected_runes:
            selected = True
        rune_dict = dict(
            [
                ("selected", selected),
                ("name", rune.get("name")),
                ("icon", f'{img_base}{rune.get("icon")}'),
                ("id", rune.get("id")),
                ("key", rune.get("key")),
                ("longDesc", rune.get("longDesc")),
            ]
        )
        if int(rune.get("slot")) == 0:
            sub_style["keystones"].append(rune_dict)
        elif int(rune.get("slot")) == 1:
            sub_style["slot_1"].append(rune_dict)
        elif int(rune.get("slot")) == 2:
            sub_style["slot_2"].append(rune_dict)
        elif int(rune.get("slot")) == 3:
            sub_style["slot_3"].append(rune_dict)

    sub_style.update(
        [
            ("name", path[0].get("style_name")),
            ("key", path[0].get("style_key")),
            ("description", path[0].get("description")),
            ("id", sub_style_id),
            ("icon", f"{img_base}{path[0].get('style_icon')}"),
        ]
    )
    return sub_style


def get_shards(page):
    shards = {
        "defense": [
            {
                "name": "5.4 bonus Attack Damage or 9 Ability Power (Adaptive)",
                "icon": f"{base_url}/dragontail-{current_version}/img/perk-images/StatMods/StatModsAdaptiveForceIcon.png",
                "selected": False,
                "id": "5001",
            },
            {
                "name": "10% bonus attack speed",
                "icon": f"{base_url}/dragontail-{current_version}/img/perk-images/StatMods/StatModsAttackSpeedIcon.png",
                "selected": True,
                "id": "5002",
            },
            {
                "name": "8 ability haste",
                "icon": f"{base_url}/dragontail-{current_version}/img/perk-images/StatMods/StatModsCDRScalingIcon.png",
                "selected": False,
                "id": "5003",
            },
        ],
        "flex": [
            {
                "name": "5.4 bonus Attack Damage or 9 Ability Power (Adaptive)",
                "icon": f"{base_url}/dragontail-{current_version}/img/perk-images/StatMods/StatModsAdaptiveForceIcon.png",
                "selected": False,
                "id": "5004",
            },
            {
                "name": "6 bonus armor",
                "icon": f"{base_url}/dragontail-{current_version}/img/perk-images/StatMods/StatModsArmorIcon.png",
                "selected": True,
                "id": "5005",
            },
            {
                "name": "8 bonus magic resistance",
                "icon": f"{base_url}/dragontail-{current_version}/img/perk-images/StatMods/StatModsMagicResIcon.png",
                "selected": False,
                "id": "5006",
            },
        ],
        "offense": [
            {
                "name": "5.4 bonus Attack Damage or 9 Ability Power (Adaptive)",
                "icon": f"{base_url}/dragontail-{current_version}/img/perk-images/StatMods/StatModsAdaptiveForceIcon.png",
                "selected": True,
                "id": "5007",
            },
            {
                "name": "6 bonus armor",
                "icon": f"{base_url}/dragontail-{current_version}/img/perk-images/StatMods/StatModsArmorIcon.png",
                "selected": False,
                "id": "5008",
            },
            {
                "name": "15 − 90 (based on level) bonus health",
                "icon": f"{base_url}/dragontail-{current_version}/img/perk-images/StatMods/StatModsMagicResIcon.png",
                "selected": False,
                "id": "5009",
            },
        ],
    }
    return shards


def get_rune_performance(request):
    from api.models import RuneStatistics
    from .rune_api_sample import data as rune_performance_data
    from django.db.models import F

    filter_args = get_filters(request)
    rune_builds = (
        RuneStatistics.objects.filter(**filter_args)
        .annotate(
            primary_style=F("rune_page_id__primary_style"),
            key_stone=F("rune_page_id__key_stone"),
            primary_perk0_1=F("rune_page_id__primary_perk0_1"),
            primary_perk0_2=F("rune_page_id__primary_perk0_2"),
            primary_perk0_3=F("rune_page_id__primary_perk0_3"),
            shard1=F("rune_page_id__shard1"),
            shard2=F("rune_page_id__shard2"),
            shard3=F("rune_page_id__shard3"),
            secondary_style=F("rune_page_id__secondary_style"),
            secondary_perk0_1=F("rune_page_id__secondary_perk0_1"),
            secondary_perk0_2=F("rune_page_id__secondary_perk0_2"),
        )
        .order_by("-winrate")[:5]
        .values()
    )
    builds = list()
    for rune_build in rune_builds:
        rune_page = dict(
            [
                ("pickRate", rune_build.get("pickrate")),
                ("winRate", rune_build.get("winrate")),
                ("primaryStyle", get_primary_style(rune_build)),
                ("subStyle", get_sub_style(rune_build)),
                ("shards", get_shards(rune_build)),
            ]
        )
        builds.append(rune_page)

    return JsonResponse({"runes": builds})


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
        filter_args.update(championId=key)

    if request.GET.get("duration"):
        fields = dict(
            [
                ("1", "All"),
                ("2", "0-25 mins"),
                ("3", "26-35 mins"),
                ("4", ">35 mins"),
            ]
        )
        filter_args.update(duration=fields.get(request.GET.get("duration")))
    else:
        filter_args.update(duration="All")

    return filter_args
