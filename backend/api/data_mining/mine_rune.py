import os
import requests
from api.models.runes import Rune
from api.models.runes_path import RunePath


def get_prepare_write_updated_rune_data(update_version):
    data = requests.get(
        f"https://ddragon.leagueoflegends.com/cdn/{update_version}/data/en_US/runesReforged.json"
    ).json()
    with open("rune_data_version.txt", "w") as rune_data_version:
        rune_data_version.write(update_version)
        for json in data:
            runepath = RunePath.objects.get(id=json["id"])
            if runepath is None:
                print(
                    f'{json["id"]} is not in the database, make sure you run the script for runepath before running this!'
                )
                break
            for slot in json["slots"]:
                for rune in slot["runes"]:
                    id = str(rune["id"])
                    rune.pop("id", None)
                    rune["pathid"] = runepath
                    rune["version"] = update_version
                    Rune.objects.update_or_create(id=id, defaults=rune)
    return None


def get_updated_rune_data(force_update=False):
    if not force_update:
        if os.path.isfile("rune_data_version.txt") and Rune.objects.exists():
            with open("rune_data_version.txt", "r") as rune_data_version:
                local_version = rune_data_version.read()
                remote_version = requests.get(
                    "https://ddragon.leagueoflegends.com/api/versions.json"
                ).json()[0]
                if local_version == remote_version:
                    return None
                else:
                    get_prepare_write_updated_rune_data(remote_version)
        get_prepare_write_updated_rune_data(
            requests.get(
                "https://ddragon.leagueoflegends.com/api/versions.json"
            ).json()[0]
        )
    get_prepare_write_updated_rune_data(
        requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]
    )
    return None
