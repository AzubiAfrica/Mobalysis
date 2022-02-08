import os
import csv
import requests
from api.models.champions import champions


def get_prepare_write_updated_champ_data(remote_version) -> None:
    """
    this is a function to get LOL champ data and write it to csv file, this function is meant to be run when
    check_champ_data_version() detects a new version of the champ data
    """
    response = requests.get(
        f"https://ddragon.leagueoflegends.com/cdn/{remote_version}/data/en_US/champion.json"
    )
    data = response.json()
    champ_data = data["data"]
    headers = data["data"]["Aatrox"].keys()
    with open("champ_data", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for champ in champ_data:
            (champ_data[champ])["version"] = remote_version
            writer.writerow(champ_data[champ])

            champions.objects.update_or_create(id=champ, defaults=champ_data[champ])
    return None


def check_champ_data_version() -> None:
    """
    this function is meant to check if the champ data has be updated on the remote server, if it detects an updated,
    the calls get_prepare_write_updated_champ_data() to update the champ data, else everything remail the same
    """
    if os.path.isfile("champ_data"):
        with open("champ_data") as csvfile:
            reader = csv.DictReader(csvfile)
            local_verson = ""
            for row in reader:
                if row["version"]:
                    local_verson = row["version"]
                    break
            remote_version = requests.get(
                "https://ddragon.leagueoflegends.com/api/versions.json"
            ).json()[0]
            if local_verson != remote_version:
                return get_prepare_write_updated_champ_data(remote_version)
            return None
    return get_prepare_write_updated_champ_data(
        requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]
    )
