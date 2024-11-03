import requests


def get_puuid(username, tagline, api_key):
    puuid_url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{username}/{tagline}"
    payload = {"api_key": api_key}
    return requests.get(puuid_url, params=payload).json()["puuid"]


class Player:
    def __init__(self, username, tagline, api_key):
        self.username = username
        self.tagline = tagline
        self.api_key = api_key
        self.puuid = get_puuid(username, tagline, api_key)

    def __str__(self):
        return f"{self.username}#{self.tagline}"

    def __repr__(self):
        return f"Player({self.username}, {self.tagline}, {self.api_key})"
