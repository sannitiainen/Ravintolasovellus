from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import psycopg2

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
