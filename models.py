from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import Serializer
from datetime import datetime

db = SQLAlchemy()

class Event(db.Model, Serializer):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=True)  
    event_datetime = db.Column(db.DateTime, default=datetime.utcnow)  # New date and time column

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'category': self.category,
            'event_datetime': self.event_datetime.strftime('%Y-%m-%d %H:%M:%S') if self.event_datetime else None
        }
