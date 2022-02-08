import json
from django.http import HttpResponse
from rest_framework import status, viewsets, views, generics
from rest_framework.response import Response
from api.models.champions import champions
from api.serializers.champions import ChampionsSerializer
from api.data_mining.mine_champ import check_champ_data_version
from api.data_mining.mine_item import get_updated_item_data
from api.data_mining.mine_rune import get_updated_rune_data
from api.data_mining.mine_rune_path import get_updated_rune_path_data
# from django.db import connection

# Create your views here.


class ChampionListingAPI(generics.GenericAPIView):
    # filterset_fields = ('name', 'region')
    serializer_class = ChampionsSerializer

    def get(self, request, format=None):

        # with connection.cursor() as cursor:
        #     cursor.execute("DROP SCHEMA public CASCADE;")
        #     cursor.execute("CREATE SCHEMA public;")
        '''
        return all champions data in the database, you just have to hit this endpoint.
        response:
        {
            "id": "Akali",
            "name": "Akali",
            "version": "11.18.1",
            "key": "84",
            "title": "the Rogue Assassin",
            "blurb": "Abandoning the Kinkou Order and her title of the Fist of Shadow, Akali now strikes alone, ready to be the deadly weapon her people need. Though she holds onto all she learned from her master Shen, she has pledged to defend Ionia from its enemies, one...",
            "info": {
            "magic": 8,
            "attack": 5,
            "defense": 3,
            "difficulty": 7
        },
        '''
        champion = champions.objects.all()
        serializer = ChampionsSerializer(champion, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChampionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChampionDataAPI(views.APIView):
    '''
    an API endpoint to create and insert champion data into the champion model, the backend of this API is the mine_champ.py
    which handles when to update the model or insert new data into the model
    '''
    def get(self, request, format=None):
        check_champ_data_version()
        return HttpResponse(status=status.HTTP_200_OK)


class ItemDataAPI(views.APIView):
    '''
    an API endpoint to create a insert item data into the item model, the backend of this API is the mine_item.py
    which handles when to update the model or insert new data into the model
    '''
    def get(self, request, format=None):
        get_updated_item_data()
        return HttpResponse(status=status.HTTP_200_OK)


class RuneDataAPI(views.APIView):
    '''
    an API endpoint to create or insert runes data into the runes model, the backend of this API is the mine_rune.py
    which handles when to update the model or insert new data into the model, whiles checking if the data is up to date
    '''
    def get(self, request, format=None):
        get_updated_rune_data()
        return HttpResponse(status=status.HTTP_200_OK)


class RunePathDataAPI(views.APIView):
    '''
    an API endpoint to create or insert runes data into the runes model, the backend of this API is the mine_rune.py
    which handles when to update the model or insert new data into the model, whiles checking if the data is up to date
    '''
    def get(self, request, format=None):
        get_updated_rune_path_data()
        return HttpResponse(status=status.HTTP_200_OK)
