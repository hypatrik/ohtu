import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()
    players = []

    for player_dict in response:
        # oletetaan että tässä data on aina samassa muodossa.
        player = Player(**player_dict)

        players.append(player)

    for player in filter(lambda p: p.nationality == "FIN", players):
        print(player)

if __name__ == "__main__":
    main()
