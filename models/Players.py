import json

from db import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playerId = db.Column(db.String(80), nullable=False)
    playerName = db.Column(db.String(80), nullable=False)
    team = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(3), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    games = db.Column(db.Integer, nullable=False)
    twoPercent = db.Column(db.Float, nullable=False)
    threePercent = db.Column(db.Float, nullable=False)
    ATR = db.Column(db.Float, nullable=False)
    PPG_Ratio = db.Column(db.Float, nullable=False)
    season = db.Column(db.Integer, nullable=False)




    def to_dict(self):
        return {
            "playerName": self.playerName,
            "team": self.team,
            "position": self.position,
            "points": self.points,
            "games": self.games,
            "twoPercent": self.twoPercent,
            "threePercent": self.threePercent,
            "ATR": self.ATR,
            "PPG_Ratio": self.PPG_Ratio,
            "season": self.season,
            "playerId": self.playerId
        }




