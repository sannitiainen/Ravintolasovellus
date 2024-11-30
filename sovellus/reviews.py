
from flask import request, render_template
from db import db
import users
from sqlalchemy.sql import text

def add_review(user_id, restaurant_id, rating, comment):
    sql = text("SELECT id FROM restaurants WHERE id=:restaurant_id")
    result= db.session.execute(sql, {"restaurant_id": restaurant_id})
    restaurant_id= result.fetchone()[0]

    #user_id = users.user_id()
    #if user_id == 0:
        #return False

    sql = text("INSERT INTO reviews (user_id, restaurant_id, rating, comment) VALUES (:user_id, :restaurant_id, :rating, :comment)")
    db.session.execute(sql, {"user_id": user_id, "restaurant_id": restaurant_id, "rating": rating, "comment": comment})
    db.session.commit()
    
    return restaurant_id

def delete_review():
    #only if admin
    pass
