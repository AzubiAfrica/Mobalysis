import os
import requests
from api.models.runes_path import RunePath


def get_prepare_write_updated_rune_path_data(update_version):
    data = requests.get(f'https://ddragon.leagueoflegends.com/cdn/{update_version}/data/en_US/runesReforged.json').json()
    with open('rune_path_data_version.txt', 'w') as rune_path_data_version:
        rune_path_data_version.write(update_version)
        for runepath in data:
            id = runepath['id']
            runepath.pop('id', None)
            runepath.pop('slots', None)
            RunePath.objects.update_or_create(id=id, **runepath)
    return None


def get_updated_rune_path_data(force_update=False):
    if not force_update:
        if (os.path.isfile('rune_path_data_version.txt') and RunePath.objects.exists()):
            with open('rune_path_data_version.txt', 'r') as rune_path_data_version:
                local_version = rune_path_data_version.read()
                remote_version = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()[0]
                if (local_version == remote_version):
                    return None
                else:
                    get_prepare_write_updated_rune_path_data(remote_version)
        get_prepare_write_updated_rune_path_data(requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()[0])
    get_prepare_write_updated_rune_path_data(requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()[0])
    return None
