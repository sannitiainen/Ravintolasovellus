from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import psycopg2

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://sanni"
db = SQLAlchemy(app)
