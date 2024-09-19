from flask import Blueprint, jsonify, request

from db import db
from models.Players import Player

players_bp = Blueprint('players', __name__, url_prefix='/api')


@players_bp.route('/players', methods=['GET'])
def get_players_by_position():
    position = request.args.get('position')
    season = request.args.get('season')

    if not position:
        return jsonify({"error": "Position parameter is required"}), 400

    if season:
        query = Player.query.filter_by(season=season ,position=position)

    else:
        query = Player.query.filter_by(position=position)

    if not query or query.count() == 0:
        return jsonify({"message": "No players found for the given position and season"}), 404



    result = [player.to_dict() for player in query]
    print(result)
    for player in result:
        seasons = []
        for player_1 in query.all():
            if player_1.playerId == player['playerId']:
                if player_1.season not in seasons:
                    seasons.append(player_1.season)
        player['seasons'] = seasons
    return jsonify(result), 200

