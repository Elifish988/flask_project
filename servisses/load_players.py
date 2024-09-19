import requests
import json

from db import db
from models.Players import Player

# קורא את הדאטה בייס
def load_players_start():
    a = load_players("2022")
    b = load_players('2023')
    c = load_players('2024')

    add_players_to_db(a + b + c)

# מקבל מידע מהגסון
def load_players(year):
    url = f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={year}&&pageSize=1000"
    return requests.get(url).json()

# print(json.dumps(load_players_start()[0], indent=4))


#הכנסה לדב
def add_players_to_db(players):
    for player in players:
        new_player = Player(
            playerId=player['playerId'],
            playerName=player['playerName'],
            team=player['team'],
            position=player['position'],
            points=player['points'],
            games=player['games'],
            twoPercent=player['twoPercent'],
            threePercent=player['threePercent'],
            ATR= ATR(player['assists'] , player['turnovers']),
            PPG_Ratio= PPG_Ratio(player['points'], player['games'], players , player['position'])
    )

        db.session.add(new_player)

    db.session.commit()



# ונקציה לחישוב ATR
def ATR(assists, turnovers):
    if turnovers == 0:
        return 0
    else:
        return  assists / turnovers


# ונקציה לחישוב PPG_Ratio
def PPG_Ratio(points, games, players , position):
    points_per_gams =  points/games
    average_points = average_points_by_position(players, position)
    if average_points == 0:
        return 1
    else:
        return points_per_gams/average_points





# חישוב ממוצע כל השחקנים בעמדה לעונה
def average_points_by_position(players, position):
    total_points = 0
    players_in_position = 0

    for player in players:
        if player['position'] == position:
            total_points += player['points']

    average_points = total_points / players_in_position if players_in_position > 0 else 0
    return average_points