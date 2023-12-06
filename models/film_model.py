# models/film_model.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Film(db.Model):
    __tablename__ = 'film'

    film_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_path = db.Column(db.String(255), nullable=True)
