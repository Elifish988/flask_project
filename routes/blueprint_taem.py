from flask import Blueprint, request, jsonify
from db import db
from models.Team import Team

teams_bp = Blueprint('teams', __name__)


@teams_bp.route('/teams', methods=['POST'])
def create_team():
    data = request.get_json()

    team_name = data.get('name_team')
    player_ids = data.get('ids_player')

    new_team = Team(
        name=team_name,
        C=player_ids[0],
        PF=player_ids[1],
        SF=player_ids[2],
        SG=player_ids[3],
        PG=player_ids[4]
    )

    db.session.add(new_team)
    db.session.commit()

    return jsonify({"message": "Team created successfully!"}), 201
