import sys
from tft_api import Player


if __name__ == "__main__":
    username = sys.argv[1]
    tagline = sys.argv[2]
    api_key = sys.argv[3]
    player = Player(username, tagline, api_key)
    print(player)
