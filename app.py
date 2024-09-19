import json
import os
from flask import Flask
from db import db
from routes.blueprint import players_bp
from servisses.load_players import load_players_start, add_players_to_db

app = Flask(__name__)

# יצירת הדאטה בייס
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_file = 'actors.db'

# היתחול הדאטה בייס
db.init_app(app)

with app.app_context():
    db.create_all()
    # players = load_players_start()
    with open('nba_players_data.json', 'r') as f:
        players = json.load(f)
        add_players_to_db(players)




# קריאה לבלו פרינט
app.register_blueprint(players_bp)

if __name__ == '__main__':
    app.run()
