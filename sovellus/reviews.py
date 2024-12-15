
from flask import request, render_template
from db import db
import users
from sqlalchemy.sql import text

def add_review(user_id, restaurant_id, rating, comment):
    sql = text("SELECT id FROM restaurants WHERE id=:restaurant_id")
    result= db.session.execute(sql, {"restaurant_id": restaurant_id})
    restaurant_id= result.fetchone()[0]

    sql = text("INSERT INTO reviews (user_id, restaurant_id, rating, comment, visible) VALUES (:user_id, :restaurant_id, :rating, :comment, :visible)")
    db.session.execute(sql, {"user_id": user_id, "restaurant_id": restaurant_id, "rating": rating, "comment": comment, "visible": 1})
    db.session.commit()

    update_rating(restaurant_id)
    
    return restaurant_id

def update_rating(restaurant_id):
    sql = text("SELECT AVG(rating) AS avg_rating FROM reviews WHERE restaurant_id = :restaurant_id")
    result = db.session.execute(sql, {"restaurant_id": restaurant_id})
    avg_rating = result.fetchone().avg_rating

    sql_update = text("UPDATE restaurants SET avg_rating = :avg_rating WHERE id = :restaurant_id;")
    db.session.execute(sql_update, {"avg_rating": avg_rating, "restaurant_id": restaurant_id})
    db.session.commit()

    return float(avg_rating)

def list_reviews(restaurant_id):
    sql = text("SELECT id, user_id, rating, comment FROM reviews WHERE restaurant_id = :restaurant_id;")
    result = db.session.execute(sql, {"restaurant_id": restaurant_id})
    reviews = list(result.fetchall())

    review_list = []

    for review in reviews:
        id = review[1]
        sql_username = text("SELECT username FROM users WHERE id = :id")
        u_name = db.session.execute(sql_username, {"id": id}).fetchone()[0]
        review_list.append({"id": review[0], "username": u_name, "rating": review[2], "comment": review[3]})

    return review_list


def delete_review(review_id):
    sql = text("UPDATE reviews SET visible=0 WHERE id = :review_id;")
    db.session.execute(sql, {"review_id": review_id})
    db.session.commit()
    return True
