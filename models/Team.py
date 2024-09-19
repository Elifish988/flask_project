from db import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    C = db.Column(db.Integer, unique=True, nullable=False)
    PF =db.Column(db.Integer, unique=True, nullable=False)
    SF = db.Column(db.Integer, unique=True, nullable=False)
    SG = db.Column(db.Integer, unique=True, nullable=False)
    PG = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return f"<Team( name={self.name} players={ f'C={self.C}, PF={self.PF}, SF={self.SF}, SG={self.SG}, PG={self.PG}'})>"