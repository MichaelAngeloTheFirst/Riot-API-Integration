import sys
from tft_api import get_puuid


if __name__ == '__main__':
    puuid = get_puuid(sys.argv[1], sys.argv[2], sys.argv[3])
    print(puuid)



