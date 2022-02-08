import os
import requests
from api.models.items import item


def get_prepare_write_updated_item_data(update_version) -> None:
    """
    this is a function to get LOL item data and write the version num to a txt file, this function is meant to be run when
    get_updated_item_data() detects a new version of the item data on the remote server
    """
    response = requests.get(
        f"https://ddragon.leagueoflegends.com/cdn/{update_version}/data/en_US/item.json"
    )
    data = response.json()
    item_data = data["data"]
    basic = {
        "name": "",
        "gold": {},
        "description": "",
        "plaintext": "",
        "consumed": False,
        "stacks": 1,
        "depth": 1,
        "consumeOnFull": False,
        "frrom": [],
        "into": [],
        "specialRecipe": 0,
        "inStore": True,
        "hideFromAll": False,
        "requiredChampion": "",
        "requiredAlly": "",
        "stats": {},
        "tags": [],
        "maps": {},
        "effect": {},
    }
    with open("item_data_version.txt", "w") as item_data_version:
        item_data_version.write(str(data["version"]))
        for item_num in item_data:
            item_data[item_num].pop("colloq")
            item_data[item_num]["frrom"] = item_data[item_num].pop("from", None)
            merged_item_data = {
                k: (item_data[item_num].get(k) or basic.get(k))
                for k in set(item_data[item_num]) | set(basic)
            }
            merged_item_data["version"] = str(data["version"])
            item.objects.update_or_create(id=item_num, defaults=merged_item_data)
    return None


def get_updated_item_data() -> None:
    """
    this function is meant to check if the item data has be updated on the remote server, if it detects an updated,
    the calls get_prepare_write_updated_item_data() to update the item data, else everything remail the same
    """
    if os.path.isfile("item_data_version.txt") and item.objects.exists():
        with open("item_data_version.txt") as item_data_version:
            local_version = item_data_version.read()
            remote_version = requests.get(
                "https://ddragon.leagueoflegends.com/api/versions.json"
            ).json()[0]
            if local_version != remote_version:
                get_prepare_write_updated_item_data(remote_version)
            return None
    get_prepare_write_updated_item_data(
        requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]
    )
    return None


# get_prepare_write_updated_item_data()
# def check_champ_data_version() -> None:

#     if os.path.isfile('champ_data_version.txt'):
#         with open('champ_data_version.txt') as csvfile:
#             reader = csv.DictReader(csvfile)
#             local_verson = ''
#             for row in reader:
#                 if row['version']:
#                     local_verson = row['version']
#                     break
#             remote_version = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()[0]
#             if local_verson != remote_version:
#                 return get_prepare_write_updated_champ_data()
#             return None
#     return get_prepare_write_updated_champ_data()


# def get_prepare_insert_or_update_champ_data() -> None:
#     response = requests.get('https://ddragon.leagueoflegends.com/cdn/11.16.1/data/en_US/champion.json')
#     data = response.json()
#     champ_data = data['data']
#     for champ in champ_data:
#         champions.objects.update_or_create(id=champ, defaults=champ_data[champ])
#     return None
