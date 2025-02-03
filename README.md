# EventMingle-App

# Events Flask API

This is a Flask-based API for managing events. It supports CRUD operations for event resources and uses Flask-Migrate for database migrations. The API interacts with a database to store and retrieve events, and includes features for handling event data such as name, location, category, and datetime.

## Technologies Used

- **Flask**: A lightweight Python web framework for building APIs.
- **Flask-RESTful**: An extension for Flask that simplifies the creation of REST APIs.
- **Flask-Migrate**: Handles SQLAlchemy database migrations.
- **Flask-CORS**: A Flask extension for handling Cross-Origin Resource Sharing (CORS).
- **dotenv**: Loads environment variables from a `.env` file.
- **SQLAlchemy**: ORM for handling database interactions.
- **SQLAlchemy-Serializer**: A library to serialize SQLAlchemy models to JSON.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Events.git
   cd Events
