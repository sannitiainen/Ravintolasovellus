
from flask import request, render_template
from db import db
import users
from sqlalchemy.sql import text

def add_review(name, rating, comment):
    restaurant_name = request.form["name"]
    sql = text("SELECT id FROM restaurants WHERE name:= restaurant_name")
    result= db.session.execute(sql, {"username": restaurant_name})
    r_id= result.fetchone()

    user_id = users.user_id()
    if user_id == 0:
        return False

    sql = text("INSERT INTO reviews (user_id, restaurant_id, rating, comment) VALUES (:user_id, :restaurant_id, :rating, :comment)")
    db.session.execute(sql, {"name": name, "rating": rating, "comment": comment})
    db.session.commit()

    sql2 = text("SELECT id FROM restaurants WHERE name LIKE :name")
    restaurant_id = db.session.execute(sql2, {"name": name}).fetchone()
    
    return restaurant_id[0]

def delete_review():
    #only if admin
    pass
