from flask_restful import Resource
from models import db, Event
from flask import request, jsonify
from datetime import datetime

class EventListResource(Resource):
    def get(self):
        events = Event.query.all()
        return jsonify([event.to_dict() for event in events])

    def post(self):
        data = request.get_json()
        if not data or not all(key in data for key in ("name", "location", "category")):
            return {"error": "Missing required fields"}, 400
        
        # Check if event_datetime exists and is valid
        event_datetime = None
        if "event_datetime" in data and data["event_datetime"]:
            try:
                event_datetime = datetime.strptime(data["event_datetime"], '%Y-%m-%d %H:%M:%S')
            except ValueError:
                return {"error": "Invalid datetime format. Use YYYY-MM-DD HH:MM:SS"}, 400

        new_event = Event(
            name=data["name"],
            location=data["location"],
            category=data["category"],
            event_datetime=event_datetime  # Set event date/time
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify(new_event.to_dict()), 201

class EventResource(Resource):
    def get(self, id):
        event = Event.query.get(id)
        if not event:
            return {"message": "Event not found"}, 404
        return event.to_dict(), 200
    
    def patch(self, id):
        data = request.get_json()
        event = Event.query.get(id)
        if not event:
            return {"error": "Event you are trying to update is not found"}, 404
        
        if "name" in data:
            event.name = data["name"]
        if "location" in data:
            event.location = data["location"]
        if "category" in data:
            event.category = data["category"]
        if "event_datetime" in data:
            if data["event_datetime"] is None:
                event.event_datetime = None  # Reset to NULL
            else:
                try:
                    event.event_datetime = datetime.strptime(data["event_datetime"], '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    return {"error": "Invalid datetime format. Use YYYY-MM-DD HH:MM:SS"}, 400

        db.session.commit()
        return event.to_dict(), 200

    def delete(self, id):
        event = Event.query.get(id)
        if not event:
            return {"error": "Event you are trying to delete does not exist"}, 404
        db.session.delete(event)
        db.session.commit()
        return {"message": "Event deleted successfully"}, 200
