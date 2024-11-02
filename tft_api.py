import requests



def get_puuid(username, tagline, api_key):
    puuid_url = f'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{username}/{tagline}'
    payload = {'api_key': api_key}
    return requests.get(puuid_url, params=payload).json()['puuid']

