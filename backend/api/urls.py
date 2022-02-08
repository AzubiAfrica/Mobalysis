from django.urls import path, include
from django.urls.resolvers import URLPattern
from rest_framework import routers
from api.views.champion_listing import (
    ChampionDataAPI,
    ItemDataAPI,
    RuneDataAPI,
    RunePathDataAPI,
    ChampionListingAPI,
)
from api.views.spells_listing import SpellListingAPI, SpellDataAPI
from api.views.champs import index, champion_overview
from api.views.runes import get_rune_performance
from api.views.champbeta import Champ
from api.views.items import item_index, get_best_item_build
from rest_framework import permissions
from api.views.spells import spell_stats
from api.views.skill_orders import skill_order_api

router = routers.DefaultRouter()
app_name = "api"
urlpatterns = [
    # path('', include(router.urls)),
    path("champs/", index, name="index"),
    path("champs/summary", champion_overview, name="champion_overview"),
    path("runes/performance", get_rune_performance, name="rune_performance"),
    path("champ", Champ.as_view(), name="champ"),
    path("items/", item_index, name="item_index"),
    path("champions/", ChampionListingAPI.as_view(), name="champion-listing"),
    path("champsdataupdate/", ChampionDataAPI.as_view(), name="champs-data"),
    path("itemsdataupdate/", ItemDataAPI.as_view(), name="item-data"),
    path("runesdataupdate/", RuneDataAPI.as_view(), name="rune-data"),
    path("runepathdataupdate/", RunePathDataAPI.as_view(), name="rune-path-data"),
    path("spelldataupdate/", SpellDataAPI.as_view(), name="spell-data"),
    path("spellstats", spell_stats, name="spell-stats"),
    path("skillorder", skill_order_api, name="skillorder"),
    path("itembuild", get_best_item_build, name="itembuild"),
    path("", include(router.urls)),
]

# urlpatterns = router.urls
