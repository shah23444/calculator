import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "calculator_secret_key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Initialize SQLAlchemy with the app
db.init_app(app)

with app.app_context():
    # Import models here to ensure they are registered with SQLAlchemy
    import models
    db.create_all()

# Import routes after db initialization
from routes import init_app
init_app(app)
