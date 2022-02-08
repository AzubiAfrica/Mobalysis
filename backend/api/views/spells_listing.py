import json
from django.http import HttpResponse
from rest_framework import status, viewsets, views, generics
from rest_framework.response import Response
from api.models.spells import Spell
from api.serializers.spells import SpellsSerializer
from api.data_mining.mine_spell import get_updated_spell_data


# Create your views here.


class SpellListingAPI(generics.GenericAPIView):
    # filterset_fields = ('name', 'region')
    serializer_class = SpellsSerializer
    '''
    list all the spell data in the database, this endpoint requires nothing
    '''
    def get(self, request, format=None):
        spells = Spell.objects.all()
        serializer = SpellsSerializer(spells, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        '''
        create a new spell and return the spell data, you have to pass the required field data
        '''
        serializer = SpellsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpellDataAPI(views.APIView):
    '''
    an API endpoint to create and insert champion data into the champion model, the backend of this API is the mine_champ.py
    which handles when to update the model or insert new data into the model
    '''
    def get(self, request, format=None):
        get_updated_spell_data()
        return HttpResponse(status=status.HTTP_200_OK)


# class ItemDataAPI(views.APIView):
#     '''
#     an API endpoint to create a insert item data into the item model, the backend of this API is the mine_item.py
#     which handles when to update the model or insert new data into the model
#     '''
#     def get(self, request, format=None):
#         get_updated_item_data()
#         return HttpResponse(status=status.HTTP_200_OK)


# class RuneDataAPI(views.APIView):
#     '''
#     an API endpoint to create or insert runes data into the runes model, the backend of this API is the mine_rune.py
#     which handles when to update the model or insert new data into the model, whiles checking if the data is up to date
#     '''
#     def get(self, request, format=None):
#         get_updated_rune_data()
#         return HttpResponse(status=status.HTTP_200_OK)


# class RunePathDataAPI(views.APIView):
#     '''
#     an API endpoint to create or insert runes data into the runes model, the backend of this API is the mine_rune.py
#     which handles when to update the model or insert new data into the model, whiles checking if the data is up to date
#     '''
#     def get(self, request, format=None):
#         get_updated_rune_path_data()
#         return HttpResponse(status=status.HTTP_200_OK)
