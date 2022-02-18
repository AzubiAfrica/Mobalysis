from api.models.summoner import summoner
from django.contrib import admin
from api.models.champion_match_bans import champion_match_bans
from api.models.champion_match_performance import champion_match_performance
from api.models.champions import champions
from api.models.durations import durations
from api.models.game_modes import game_modes
from api.models.matches import matches
from api.models.ranks import rank
from api.models.tier import tier
from api.models.regions import regions
from api.models.items import item
from api.models.runes import Rune
from api.models.runes_path import RunePath
from api.models.rune_page import RunePage
from api.models.spells import Spell
from api.models.item_match_performance import item_match_performance
from api.models.spell_match_performance import spell_match_performance
from api.models.rune_match_performance import rune_match_performance
from api.models.item_property import item_property
from api.models.spell_stats import spells_stats
from api.models.filter_combinations import FilterCombination


# Register your models here.


class ChampionMatchBansAdmin(admin.ModelAdmin):
    list_display = ("id", "gameId", "championId")


class ChampionMatchPerformanceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "gameId",
        "championId",
        "summonerId",
        "champLevel",
        "win",
        "role",
        "lane",
        "kills",
        "deaths",
        "assists",
        "pentakills",
        "platformId",
        "gameMode",
    )


class ChampionsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image")


class DurationsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "minimumTime", "maximumTime")


class GameModesAdmin(admin.ModelAdmin):
    list_display = ["name"]


class MatchesAdmin(admin.ModelAdmin):
    list_display = (
        "gameId",
        "platformId",
        "gameCreation",
        "gameDuration",
        "queueId",
        "seasonId",
        "gameVersion",
        "gameMode",
        "gameType",
    )


class TierAdmin(admin.ModelAdmin):
    list_display = ("name",)


class RankAdmin(admin.ModelAdmin):
    list_display = ("tierRank",)


class RegionsAdmin(admin.ModelAdmin):
    list_display = ("platformId",)


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "effect",
        "plaintext",
        "into",
        "image",
        "gold",
        "tags",
        "maps",
        "stats",
        "depth",
        "specialRecipe",
        "stacks",
        "consumeOnFull",
        "hideFromAll",
        "inStore",
        "consumed",
        "requiredAlly",
        "requiredChampion",
        "rune",
    )


class ItemMatchPerformanceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "gameId",
        "itemId",
        "championId",
        "platformId",
        "summonerId",
        "tier",
        "win",
        "gameMode",
    )


class RunePathAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "key",
        "icon",
        "name",
    )


class RuneAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "key",
        "pathid",
        "icon",
        "name",
        "shortDesc",
        "longDesc",
    )


class SpellAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "tooltip",
        "maxrank",
        "cooldown",
        "cooldownBurn",
        "cost",
        "costBurn",
        "datavalues",
        "effect",
        "effectBurn",
        "vars",
        "key",
        "summonerLevel",
        "modes",
        "costType",
        "maxammo",
        "range",
        "rangeBurn",
        "image",
        "resource",
    )


class SpellMatchPerformanceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "gameId",
        "spellId",
        "championId",
        "summoner_level",
        "tier_id",
        "summoner_id",
        "win",
        "gameMode",
        "champLevel",
    )


class RuneMatchPerformanceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "gameId",
        "runeId",
        "runepathId",
        "championId",
        "summonerId",
        "summoner_level",
        "tier_id",
        "platformId",
        "win",
        "gameMode",
        "champLevel",
    )
class RunePageAdmin(admin.ModelAdmin):
    list_display = (
        "rune_page_id",
        "primary_style",
        "key_stone",
        "primary_perk0_1",
        "primary_perk0_2",
        "primary_perk0_3",
        "shard1",
        "shard2",
        "shard3",
        "secondary_style",
        "secondary_perk0_1",
        "secondary_perk0_2",
    )

class ItemPropertyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "itemId",
        "attribute_name",
        "attribute_value",
    )


class SpellStatsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "spells",
        "championid",
        "region",
        "tier",
        "fgm",
        "role",
        "winrate",
        "pickrate",
    )

class FilterCombinationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "filter_id",
        "filter_value")


admin.site.register(champion_match_bans, ChampionMatchBansAdmin)
admin.site.register(champion_match_performance, ChampionMatchPerformanceAdmin)
admin.site.register(champions, ChampionsAdmin)
admin.site.register(durations, DurationsAdmin)
admin.site.register(game_modes, GameModesAdmin)
admin.site.register(matches, MatchesAdmin)
admin.site.register(rank, RankAdmin)
admin.site.register(tier, TierAdmin)
admin.site.register(regions, RegionsAdmin)
admin.site.register(item, ItemAdmin)
admin.site.register(Rune, RuneAdmin)
admin.site.register(RunePage, RunePageAdmin)
admin.site.register(RunePath, RunePathAdmin)
admin.site.register(Spell, SpellAdmin)
admin.site.register(item_match_performance, ItemMatchPerformanceAdmin)
admin.site.register(spell_match_performance, SpellMatchPerformanceAdmin)
admin.site.register(rune_match_performance, RuneMatchPerformanceAdmin)
admin.site.register(item_property, ItemPropertyAdmin)
admin.site.register(spells_stats, SpellStatsAdmin)
admin.site.register(FilterCombination, FilterCombinationAdmin)