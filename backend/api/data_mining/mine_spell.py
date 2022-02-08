import os
import requests
from api.models.spells import Spell


def get_prepare_write_updated_spell_data(update_version):
    summonerspell = requests.get(f'https://ddragon.leagueoflegends.com/cdn/{update_version}/data/en_US/summoner.json').json()
    with open('spell_data_version.txt', 'w') as spell_data_version:
        spell_data_version.write(update_version)
        for spell in summonerspell["data"]:
            # print(summonerspell["data"][spell]["name"])
            key = summonerspell["data"][spell]["key"]
            spell_data = summonerspell["data"][spell]
            spell_data.pop("key")
            spell_data['effect'].pop(0)
            Spell.objects.update_or_create(key=key, **spell_data)
    return None


def get_updated_spell_data(force_update=False):
    if not force_update:
        if (os.path.isfile('spell_data_version.txt') and Spell.objects.exists()):
            with open('spell_data_version.txt', 'r') as spell_data_version:
                local_version = spell_data_version.read()
                remote_version = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()[0]
                if (local_version == remote_version):
                    return None
                else:
                    get_prepare_write_updated_spell_data(remote_version)
        get_prepare_write_updated_spell_data(requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()[0])
    get_prepare_write_updated_spell_data(requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()[0])
    return None
