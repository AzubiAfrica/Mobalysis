from django.http import JsonResponse
from api.models.champions import champions
from api.serializers.champions import ChampionsSerializer
from rest_framework import viewsets
from api.models.items import item
from api.serializers.items import ItemsSerializer


class ChampionsDataJsonAPI(viewsets.ModelViewSet):
    queryset = champions.objects.all()
    serializer_class = ChampionsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

class ChampionsDataAPI(viewsets.ModelViewSet):
    queryset = champions.objects.all()
    serializer_class = ChampionsSerializer
    http_method_names = ["get", "head","options"]


class ItemsDataAPI(viewsets.ModelViewSet):
    queryset = item.objects.all()
    serializer_class = ItemsSerializer
    http_method_names = ["get", "head","options"]

