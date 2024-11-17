
from flask import request, render_template, result
from db import db
import users

def add_review():
    restaurant_name = request.form["name"]
    sql = "SELECT id FROM restaurants WHERE name:= restaurant_name"
    result= db.session.execute(sql, {"username": restaurant_name})
    r_id= result.fetchone()

    user_id = users.user_id()
    if user_id == 0:
        return False

    sql = "InSERT INTO reviews (user_id, restaurant_id, rating, comment) VALUES (:user_id, :restaurant_id, :rating, :comment)"
    db.session.execute(sql, {""})

def delete_review():
    #only if admin
    pass
