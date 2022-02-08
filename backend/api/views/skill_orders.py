from django.http import JsonResponse
from api.views.filter_combinations import get_filters
from api.models.champion_spells import ChampionSpell
from .assets import base_url, current_version


def skill_order_api(request):
    from api.models import SkillOrders
    from django.db.models import F, ExpressionWrapper, DecimalField

    filter_args = get_filters(request)
    skillorders = (
        SkillOrders.objects.filter(**filter_args)
        .annotate(
            games_won=ExpressionWrapper(
                F("games_played") * F("winrate"), output_field=DecimalField()
            ),
        )
        .order_by("-games_won")[:1]
        .values()
    )

    data = list()
    champion = request.GET.get("champion")
    image_url = f"{base_url}/dragontail-{current_version}/{current_version}/img/spell/"
    all_spells = (
        ChampionSpell.objects.filter(champion_id=champion)
        .values("name", "description", "image")
        .annotate(id=F("spell_id"))
    )

    for stat in skillorders:
        try:
            data.append(
                [
                    {
                        **all_spells[0],
                        "image": f'{image_url}{all_spells[0]["image"]}',
                        "levels": [
                            stat["spell_1_level_1"],
                            stat["spell_1_level_2"],
                            stat["spell_1_level_3"],
                            stat["spell_1_level_4"],
                            stat["spell_1_level_5"],
                            stat["spell_1_level_6"],
                        ],
                    },
                    {
                        **all_spells[1],
                        "image": f'{image_url}{all_spells[1]["image"]}',
                        "levels": [
                            stat["spell_2_level_1"],
                            stat["spell_2_level_2"],
                            stat["spell_2_level_3"],
                            stat["spell_2_level_4"],
                            stat["spell_2_level_5"],
                            stat["spell_2_level_6"],
                        ],
                    },
                    {
                        **all_spells[2],
                        "image": f'{image_url}{all_spells[2]["image"]}',
                        "levels": [
                            stat["spell_3_level_1"],
                            stat["spell_3_level_2"],
                            stat["spell_3_level_3"],
                            stat["spell_3_level_4"],
                            stat["spell_3_level_5"],
                            stat["spell_3_level_6"],
                        ],
                    },
                    {
                        **all_spells[3],
                        "image": f'{image_url}{all_spells[3]["image"]}',
                        "levels": [
                            stat["spell_4_level_1"],
                            stat["spell_4_level_2"],
                            stat["spell_4_level_3"],
                            stat["spell_4_level_4"],
                            stat["spell_4_level_5"],
                            stat["spell_4_level_6"],
                        ],
                    },
                ]
            )
        except:
            return JsonResponse({"data": []})

    return JsonResponse({"data": data})
