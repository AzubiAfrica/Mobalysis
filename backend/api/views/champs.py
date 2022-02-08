from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render

from .regions import regions
from .assets import current_version, base_url


def get_champion_stats_filters(request):
    from api.models.champions import champions

    filter_args_champion_stats = dict()

    if request.GET.get("region"):
        fields = regions
        filter_args_champion_stats.update(region=fields.get(request.GET.get("region")))
    else:
        filter_args_champion_stats.update(region="All")

    if request.GET.get("fgm"):
        fields = dict(
            [
                ("1", "All"),
                ("2", "ARAM"),
                ("3", "URF"),
                ("4", "CLASSIC"),
            ]
        )
        filter_args_champion_stats.update(fgm=fields.get(request.GET.get("fgm")))
    else:
        filter_args_champion_stats.update(fgm="All")

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
        filter_args_champion_stats.update(tier=fields.get(request.GET.get("tier")))
    else:
        filter_args_champion_stats.update(tier="All")

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
        filter_args_champion_stats.update(role=fields.get(request.GET.get("role")))
    else:
        filter_args_champion_stats.update(role="All")

    if request.GET.get("champion"):
        champion_id = request.GET.get("champion")
        if champion_id != "All":
            champion = champions.objects.get(id__iexact=champion_id)
            key = champion.key
            filter_args_champion_stats.update(championid=key)



    return filter_args_champion_stats


def index(request):
    from api.models.champion_match_performance import champion_match_performance
    from api.models.champion_match_bans import champion_match_bans
    from api.models.matches import matches
    from api.models.champions import champions
    from api.models.champions_stats import ChampionsStats
    from django.db.models import F, Avg, Count, Sum
    from django.core.exceptions import ObjectDoesNotExist

    filter_args_champion_stats = get_champion_stats_filters(request)
    try:
        champion_stats = ChampionsStats.objects.filter(
            **filter_args_champion_stats
        ).values()
    except IndexError:
        champion_stats = None
    champion_data = list()
    for stat in champion_stats:
        champion_id = stat.get("championid")
        try:
            champion = champions.objects.get(key=champion_id)
        except ObjectDoesNotExist:
            continue
        image = champion.image.get("full")
        KDA = f"""{round(stat.get("kills"),1)}/{round(stat.get("deaths"),1)}/{round(stat.get("assists"),1)}"""
        stats = dict()
        stats.update(championId=champion.key)
        stats.update(title=champion.title)
        stats.update(blurb=champion.blurb)
        stats.update(name=champion.name)
        stats.update(key=champion.key)
        stats.update(id=champion.id)
        stats.update(
            image=f"""{base_url}/dragontail-{current_version}/{current_version}/img/champion/{image}"""
        )
        stats.update(KDA=KDA)
        stats.update(banRate=round(float(stat.get("banrate")), 1))
        stats.update(earlyGameScore=4)
        stats.update(gamesPlayed=162)
        stats.update(pickRate=round(float(stat.get("pickrate")), 1))
        stats.update(winRate=round(float(stat.get("winrate")), 1))
        stats.update(pentasMatch=round(float(stat.get("pentakills")), 1))
        champion_data.append(stats)
    return JsonResponse({"champions": champion_data})


def get_champion_bio(request):
    from api.models.champions import champions

    bio = None
    if request.GET.get("champion"):
        champion_id = request.GET.get("champion")
        champion = champions.objects.get(id__iexact=champion_id)
        name = champion.name
        image = champion.image.get("full")
        id = champion.id
        title = champion.title
        key = champion.key
        bio = {
            "name": name,
            "id": id,
            "title": title,
            "image_url": f"""{base_url}/dragontail-{current_version}/img/champion/splash/{id}_1.jpg""",
            "key": key,
            "blurb": champion.blurb,
        }
    return bio


def get_pick_rate(args=None):
    if args:
        return str(round(float(args.get("pickrate")), 1))
    return "0"


def get_win_rate(args=None):
    if args:
        return str(round(float(args.get("winrate")), 1))
    return "0"


def get_ban_rate(args=None):
    if args:
        return str(round(float(args.get("banrate")), 1))
    return "0"


# def get_mained_by(args=None):
#     if args:
#         return str(round(float(args.get("mained_by_field")), 1))
#     return "0"


def get_kills(args=None):
    if args:
        return str(round(float(args.get("kills")), 1))
    return "0"


def get_deaths(args=None):
    if args:
        return str(round(float(args.get("deaths")), 1))
    return "0"


def get_assists(args=None):
    if args:
        return str(round(float(args.get("assists")), 1))
    return "0"


def get_pentasmatch(args=None):
    if args:
        return str(round(float(args.get("pentakills")), 1))
    return "0"


def get_counters(args=None):
    return [
        {
            "id": "Graves",
            "name": "Graves",
            "image_url": f"{base_url}/dragontail-{current_version}/{current_version}/11.16.1/img/champion/Graves.png",
        },
        {
            "id": "Ahri",
            "name": "Ahri",
            "image_url": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/champion/Ahri.png",
        },
        {
            "id": "Kayle",
            "name": "Kayle",
            "image_url": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/champion/Kayle.png",
        },
    ]


def get_is_countered_by(args=None):
    return [
        {
            "id": "Fizz",
            "name": "Fizz",
            "image_url": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/champion/Fizz.png",
        },
        {
            "id": "Volibear",
            "name": "Volibear",
            "image_url": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/champion/Volibear.png",
        },
        {
            "id": "Sejuani",
            "name": "Sejuani",
            "image_url": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/champion/Sejuani.png",
        },
    ]


def get_starting_build(args=None):
    return {
        "pick_rate": "75",
        "win_rate": "45",
        "items": [
            {
                "id": "1027",
                "name": "Sapphire Crystal",
                "image": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/item/1027.png",
            },
            {
                "id": "2031",
                "name": "Refillable Potion",
                "image": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/item/2031.png",
            },
            {
                "id": "2423",
                "name": "Perfectly Timed Stopwatch",
                "image": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/item/2423.png",
            },
        ],
    }


def get_core_build(args=None):
    return {
        "pick_rate": "75",
        "win_rate": "45",
        "items": [
            {
                "id": "3031",
                "name": "Infinity Edge",
                "image": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/item/3031.png",
            },
            {
                "id": "3513",
                "name": "Eye of the Herald",
                "image": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/item/3513.png",
            },
            {
                "id": "4643",
                "name": "Vigilant Wardstone",
                "image": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/item/4643.png",
            },
        ],
    }


def get_end_build(args=None):
    return {
        "pick_rate": "75",
        "win_rate": "45",
        "items": [
            {
                "id": "8001",
                "name": "Anathema's Chains",
                "image": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/item/8001.png",
            },
            {
                "id": "6675",
                "name": "Navori Quickblades",
                "image": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/item/6675.png",
            },
            {
                "id": "6653",
                "name": "Liandry's Anguish",
                "image": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/item/6653.png",
            },
        ],
    }


def get_boots(args=None):
    return {
        "pick_rate": "75",
        "win_rate": "45",
        "items": [
            {
                "id": "2422",
                "name": "Slightly Magical Footwear",
                "image": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/item/2422.png",
            },
            {
                "id": "3009",
                "name": "Boots of Swiftness",
                "image": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/item/3009.png",
            },
            {
                "id": "3020",
                "name": "Sorcerer's Shoes",
                "image": "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/item/3020.png",
            },
        ],
    }


def get_role_performance_filters(request):
    from api.models.champions import champions

    filter_args_role_stats = dict()

    if request.GET.get("region"):
        fields = regions
        filter_args_role_stats.update(region=fields.get(request.GET.get("region")))
    else:
        filter_args_role_stats.update(region="all")

    if request.GET.get("fgm"):
        fields = dict(
            [
                ("1", "All"),
                ("2", "ARAM"),
                ("3", "URF"),
                ("4", "CLASSIC"),
            ]
        )
        filter_args_role_stats.update(fgm=fields.get(request.GET.get("fgm")))
    else:
        filter_args_role_stats.update(fgm="all")

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
        filter_args_role_stats.update(tier=fields.get(request.GET.get("tier")))
    else:
        filter_args_role_stats.update(tier="all")

    if request.GET.get("champion"):
        champion_id = request.GET.get("champion")
        if champion_id != "all":
            champion = champions.objects.get(id__iexact=champion_id)
            key = champion.key
            filter_args_role_stats.update(championid=key)

    return filter_args_role_stats


def get_champion_role_performance(request):
    from api.models import RoleStats

    role_performance_filters = get_role_performance_filters(request)
    stats = RoleStats.objects.filter(**role_performance_filters).order_by("winrate")
    performance = dict()
    if stats:
        values = stats.values()
        total_pick_rate, total_win_rate = [0, 0]
        for value in values:
            total_pick_rate += value.get("pickrate")
            total_win_rate += value.get("winrate")
        for v in values:
            try:
                vals = dict(
                    [
                        (
                            "win_rate",
                            str(round((v.get("winrate")), 0)),
                        ),
                        (
                            "ban_rate",
                            str(round((v.get("pickrate") / total_pick_rate) * 100, 0)),
                        ),
                        (
                            "pick_rate",
                            str(round((v.get("pickrate") / total_pick_rate) * 100, 0)),
                        ),
                    ]
                )
            except:
                vals = dict([])
            if v.get("role") == "mid laner":
                index_name = "mid"
                vals.update(
                    [
                        (
                            "position_icon_url",
                            f"{base_url}/positions/Position_Gold-Mid.png",
                        )
                    ]
                )
            elif v.get("role") == "Support":
                index_name = "support"
                vals.update(
                    [
                        (
                            "position_icon_url",
                            f"{base_url}/positions/Position_Gold-Support.png",
                        )
                    ]
                )
            elif v.get("role") == "top laner":
                index_name = "top"
                vals.update(
                    [
                        (
                            "position_icon_url",
                            f"{base_url}/positions/Position_Gold-Top.png",
                        )
                    ]
                )
            elif v.get("role") == "Bot":
                index_name = "bot"
                vals.update(
                    [
                        (
                            "position_icon_url",
                            f"{base_url}/positions/Position_Gold-Bot.png",
                        )
                    ]
                )
            elif v.get("role") == "jungler":
                index_name = "jungler"
                vals.update(
                    [
                        (
                            "position_icon_url",
                            f"{base_url}/positions/Position_Gold-Jungle.png",
                        )
                    ]
                )
            performance.update([(index_name, vals)])
    return performance


def get_ranked_emblem(tier):
    tier = str(tier).lower()
    emblems = dict(
        [
            ("iron", "Emblem_Iron.png"),
            ("bronze", "Emblem_Bronze.png"),
            ("silver", "Emblem_Silver.png"),
            ("gold", "Emblem_Gold.png"),
            ("platinum", "Emblem_Platinum.png"),
            ("master", "Emblem_Master.png"),
            ("grandmaster", "Emblem_Grandmaster.png"),
            ("challenger", "Emblem_Challenger.png"),
        ]
    )
    return emblems.get(tier)


def get_best_players_filters(request):
    from api.models.champions import champions

    filter_args_best_players = dict()
    if request.GET.get("region") and request.GET.get("region") != "1":
        fields = regions
        filter_args_best_players.update(
            platformid=fields.get(request.GET.get("region"))
        )

    if request.GET.get("tier") and request.GET.get("tier") != "1":
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
        filter_args_best_players.update(tier=fields.get(request.GET.get("tier")))

    if request.GET.get("fgm") and request.GET.get("fgm") != "1":
        fields = dict(
            [
                ("1", "All"),
                ("2", "ARAM"),
                ("3", "URF"),
                ("4", "CLASSIC"),
            ]
        )
        filter_args_best_players.update(fgm=fields.get(request.GET.get("fgm")))

    if request.GET.get("role") and request.GET.get("role") != "1":
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
        filter_args_best_players.update(role=fields.get(request.GET.get("role")))

    if request.GET.get("champion"):
        champion_id = request.GET.get("champion")
        if champion_id != "All":
            champion = champions.objects.get(id__iexact=champion_id)
            key = champion.key
            filter_args_best_players.update(championid=key)

    return filter_args_best_players


def get_best_players(request):
    from api.models import ChampionSummoners
    from django.db.models import F, Avg, Count, Sum, ExpressionWrapper, DecimalField

    champion_id = request.GET.get("champion")
    best_players_filters = get_best_players_filters(request)
    summoners = (
        (
            (ChampionSummoners.objects.filter(**best_players_filters)).annotate(
                games_won=ExpressionWrapper(
                    F("games_played") * F("winrate"), output_field=DecimalField()
                ),
            )
        )
        .order_by("-games_won")[:5]
        .values(
            "summonername",
            "games_won",
            "winrate",
            "games_played",
            "tier",
        )
    )

    entries = list()
    for summoner in summoners:
        entry = dict()
        entry["summoner"] = summoner.get("summonername")
        entry["tier"] = summoner.get("tier")
        entry["winrate"] = round(summoner.get("winrate"), 1)
        entry["played"] = summoner.get("games_played")
        entry["games_won"] = round(summoner.get("games_won") / 100, 0)
        entry["ranked_emblem_url"] = f"{base_url}/emblems/%s" % (
            get_ranked_emblem(summoner.get("tier"))
        )
        entries.append(entry)
    return entries




def champion_overview(request):
    from api.models.champions_stats import ChampionsStats

    bio = get_champion_bio(request)
    key = bio.get("key")
    filter_args_champion_stats = get_champion_stats_filters(request)
    try:
        stats = ChampionsStats.objects.filter(**filter_args_champion_stats).values()[0]
    except IndexError:
        stats = None

    response = {
        "champion": bio,
        "pick_rate": get_pick_rate(stats),
        "win_rate": get_win_rate(stats),
        "ban_rate": get_ban_rate(stats),
        # "mained_by": get_mained_by(stats),
        "kills": get_kills(stats),
        "deaths": get_deaths(stats),
        "assists": get_assists(stats),
        "counters": get_counters(stats),
        "is_countered_by": get_is_countered_by(stats),
        "starting_build": get_starting_build(stats),
        "core_build": get_core_build(stats),
        "end_build": get_end_build(stats),
        "boots": get_boots(stats),
        "role_performance": get_champion_role_performance(request),
        "best_players": get_best_players(request),
        # "pick_rate_history": get_pick_rate_history(request),
        # "ban_rate_history": get_ban_rate_history(request),
        # "win_rate_history": get_win_rate_history(request),
        "pentasMatch": get_pentasmatch(stats),
    }
    return JsonResponse(response)


# def get_random_rate(a, b):
#     from datetime import date, timedelta
#     import random

#     sdate = date(2021, 6, 1)  # start date
#     edate = date.today()  # end date
#     delta = edate - sdate  # as timedelta
#     rate = []
#     for i in range(delta.days + 1):
#         day = sdate + timedelta(days=i)
#         rate.append(
#             dict(
#                 [
#                     ("date", f"""{day.strftime('%d%m%Y')}"""),
#                     ("value", random.randrange(a, b)),
#                 ]
#             )
#         )
#     return rate


def get_champion_listing(request):
    pass
