import requests
import json

from db import db
from models.Players import Player

# קורא את הדאטה בייס
def load_players_start():
    a = load_players("2022")
    b = load_players('2023')
    c = load_players('2024')
    # קורא לפונקציה שמכניסה לדאטה בייס
    add_players_to_db(a + b + c)

# מקבל מידע מהגסון
def load_players(year):
    url = f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={year}&&pageSize=1000"
    result = requests.get(url)
    json_data = result.json()
    return json_data

# print(json.dumps(load_players_start()[0], indent=4))


#הכנסה לדב



def add_players_to_db(players):
    for player in players:
        for key in player.keys():
            if player.get(key) is None:
                player[key] = 0.0
        new_player = Player(
            playerId=player['playerId'],
            playerName=player['playerName'],
            team=player['team'],
            position=player['position'],
            points=player['points'],
            games=player['games'],
            season =player['season'],
            twoPercent=player.get('twoPercent', 0.0),
            threePercent=player.get('threePercent', 0.0),
            ATR=ATR(player['assists'], player['turnovers']),
            PPG_Ratio=PPG_Ratio(player['points'], player['games'], players, player['position'])
        )
        db.session.add(new_player)
    db.session.commit()

# פונקציה לחישוב ATR
def ATR(assists, turnovers):
    if turnovers == 0:
        return assists
    return assists / turnovers

# פונקציה לחישוב PPG_Ratio
def PPG_Ratio(points, games, players, position):
    points_per_game = points / games if games > 0 else 0
    average_points = average_points_by_position(players, position)
    if average_points == 0:
        return points_per_game
    return points_per_game / average_points

# חישוב ממוצע כל השחקנים בעמדה לעונה
def average_points_by_position(players, position):
    total_points = 0
    players_in_position = 0

    for player in players:
        if player['position'] == position:
            total_points += player['points']
            players_in_position += player['games']

    average_points = total_points / players_in_position if players_in_position > 0 else 0
    return average_points


