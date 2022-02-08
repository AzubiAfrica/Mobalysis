from django.http import JsonResponse
from django.shortcuts import render
from api.models.champion_match_performance import champion_match_performance
from api.models.champion_match_bans import champion_match_bans
from api.models.matches import matches
from api.models.champions import champions
from django.db.models import F, Avg, Count
from rest_framework import status, viewsets, views, generics
from api.serializers.champions import ChampionsSerializer
from api.serializers.matches import MatchesSerializer


class Champ(generics.ListAPIView):
    serializer_class = MatchesSerializer

    def get_queryset(self):
        """
        Parameters
        region -- A first parameter
        fgm -- A second parameter
        """
        filter_args_performance = dict()
        filter_args_matches = dict()
        # filter_args_matches.update(platformId=request.GET.get("region"))
        # print(filter_args_matches)
        # qs_games = matches.objects.filter(**filter_args_matches)
        # return qs_games

        if self.request.GET.get("region"):
            filter_args_matches.update(platformId=self.request.GET.get("region"))

        if self.request.GET.get("fgm"):
            filter_args_matches.update(gameMode__iexact=self.request.GET.get("fgm"))

        if self.request.GET.get("matchType"):
            filter_args_matches.update(gameType__iexact=self.request.GET.get("matchType"))

        if self.request.GET.get("matchDuration"):
            matchDuration = self.request.GET.get("matchDuration")
            if int(matchDuration) == 1:
                filter_args_matches.update(gameDuration__gte=0)
                filter_args_matches.update(gameDuration__lte=(25 * 60))
            if int(matchDuration) == 2:
                filter_args_matches.update(gameDuration__gte=(25 * 60))
                filter_args_matches.update(gameDuration__lte=(55 * 60))
            if int(matchDuration) == 3:
                filter_args_matches.update(gameDuration__gte=(35 * 60))

        if filter_args_matches:
            qs_games = matches.objects.filter(**filter_args_matches)
        else:
            qs_games = matches.objects.all()

        if self.request.GET.get("champion"):
            filter_args_performance.update(
                championId__name__iexact=self.request.GET.get("champion")
            )

        if self.request.GET.get("role"):
            filter_args_performance.update(role__iexact=self.request.GET.get("role"))

        if self.request.GET.get("lane"):
            filter_args_performance.update(lane__iexact=self.request.GET.get("lane"))

        if self.request.GET.get("champLevel"):
            filter_args_performance.update(champLevel=self.request.GET.get("champLevel"))

        filter_args_performance.update(gameId__in=qs_games)

        champion_performances = (
            champion_match_performance.objects.filter(**filter_args_performance)
            .values("championId")
            .annotate(
                kills=Avg("kills"),
                deaths=Avg("deaths"),
                assists=Avg("assists"),
                pentasMatch=Avg("pentakills"),
                winRate=Avg("win"),
                picks=Count("*"),
                name=F("championId_id__name"),
                image=F("championId_id__image"),
            )
        )
        champion_bans = (
            champion_match_bans.objects.filter(
                gameId__in=qs_games,
            )
            .values("championId")
            .annotate(bans=Count("*"))
        )
        champs = champions.objects.all()
        champion_ban_data = dict()
        champion_data = list()
        for champion_ban in champion_bans:
            champion_ban_data.update(
                {
                    champion_ban.get("championId"): round(
                        float(champion_ban.get("bans")) / float(qs_games.count()), 2
                    )
                }
            )
        for champion_performance in champion_performances:
            stats = dict()
            pickRate = float(champion_performance.get("picks")) / float(qs_games.count())
            winRate = float(champion_performance.get("picks")) / float(qs_games.count())
            kills = round(champion_performance.get("kills"), 2)
            deaths = round(champion_performance.get("deaths"), 2)
            assists = round(champion_performance.get("assists"), 2)
            pentasMatch = round(champion_performance.get("pentasMatch"), 2)
            kda = f"""{kills},{deaths},{assists}"""
            winRate = round(champion_performance.get("winRate"), 2)
            image = f"""https://earlygamestore.z13.web.core.windows.net/dragontail/11.16.1/img/champion/{champion_performance.get('image')['full']}"""
            stats.update(championId=champion_performance.get("championId"))
            stats.update(name=champion_performance.get("name"))
            stats.update(image=image)
            stats.update(KDA=kda)
            stats.update(
                banRate=champion_ban_data.get(
                    champion_performance.get("championId"), float(0)
                )
            )
            stats.update(earlyGameScore=4)
            stats.update(gamesPlayed=champion_performance.get("picks"))
            stats.update(pickRate=round(pickRate, 2))
            stats.update(rank=self.request.GET.get("rank", "All Tiers"))
            stats.update(roles=self.request.GET.get("role", "All Roles"))
            stats.update(champLevel=self.request.GET.get("champLevel", "All Champion Levels"))
            stats.update(skills="E,W,Q")
            stats.update(winRate=winRate)
            stats.update(pentasMatch=pentasMatch)
            champion_data.append(stats)
        return JsonResponse({"champions": champion_data})
