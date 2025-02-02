from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from models import db
from resources.event import EventListResource, EventResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

@app.route("/")
def home():
    return "<h1>Welcome to Events Page</h1>"


api.add_resource(EventListResource, '/events')
api.add_resource(EventResource, '/events/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
