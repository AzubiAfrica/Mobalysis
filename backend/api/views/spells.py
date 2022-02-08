from django.http import JsonResponse


def spell_stats(request):
    from api.models import SpellStats, Spell
    from django.db.models import F, ExpressionWrapper, DecimalField

    base_img_url = (
        "https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/spell/"
    )
    filter_args = get_filters(request)
    spell_builds = (
        SpellStats.objects.filter(**filter_args)
        .annotate(
            games_won=ExpressionWrapper(
                F("games_played") * F("winrate"), output_field=DecimalField()
            ),
        )
        .order_by("-games_won")[:10]
        .values()
    )

    All_spells = Spell.objects.all().values()
    spells_dict = dict()
    for a_spell in All_spells:
        spell_details = dict(
            [
                ("name", a_spell.get("name")),
                ("icon", (a_spell.get("image")).get("full")),
                ("id", a_spell.get("id")),
                ("key", a_spell.get("key")),
                ("description", a_spell.get("description")),
            ]
        )
        spells_dict.update([(a_spell.get("key"), spell_details)])

    data = list()
    for build in spell_builds:
        spell_1_id, spell_2_id = (build.get("spells")).split("_")
        spell_1_fields = spells_dict.get(spell_1_id)
        spell_2_fields = spells_dict.get(spell_2_id)
        data.append(
            dict(
                [
                    ("spell_1_name", spell_1_fields.get("name")),
                    ("spell_1_id", spell_1_fields.get("id")),
                    ("spell_1_key", spell_1_fields.get("key")),
                    ("spell_1_description", spell_1_fields.get("description")),
                    ("spell_1_icon", f'{base_img_url}{spell_1_fields.get("icon")}'),
                    ("spell_2_name", spell_2_fields.get("name")),
                    ("spell_2_id", spell_2_fields.get("id")),
                    ("spell_2_key", spell_2_fields.get("key")),
                    ("spell_2_description", spell_2_fields.get("description")),
                    ("spell_2_icon", f'{base_img_url}{spell_2_fields.get("icon")}'),
                    ("winrate", build.get("winrate")),
                    ("pickrate", build.get("pickrate")),
                ]
            )
        )
    return JsonResponse({"data": data})


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
        filter_args.update(championid=key)

    # if request.GET.get("duration"):
    #     fields = dict(
    #         [
    #             ("1", "All"),
    #             ("2", "0-25 mins"),
    #             ("3", "26-35 mins"),
    #             ("4", ">35 mins"),
    #         ]
    #     )
    #     filter_args.update(duration=fields.get(request.GET.get("duration")))
    # else:
    #     filter_args.update(duration="All")

    return filter_args
