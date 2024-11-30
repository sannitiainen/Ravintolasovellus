
from flask import request, render_template
from db import db
import users
from sqlalchemy.sql import text

def add_review(user_id, restaurant_id, rating, comment):
    sql = text("SELECT id FROM restaurants WHERE id=:restaurant_id")
    result= db.session.execute(sql, {"restaurant_id": restaurant_id})
    restaurant_id= result.fetchone()[0]

    sql = text("INSERT INTO reviews (user_id, restaurant_id, rating, comment) VALUES (:user_id, :restaurant_id, :rating, :comment)")
    db.session.execute(sql, {"user_id": user_id, "restaurant_id": restaurant_id, "rating": rating, "comment": comment})
    db.session.commit()

    update_rating(restaurant_id)
    
    return restaurant_id

def update_rating(restaurant_id):
    sql = text("SELECT rating FROM reviews WHERE restaurant_id = :restaurant_id")
    result = db.session.execute(sql, {"restaurant_id": restaurant_id})
    ratings_list = list(result.fetchall())

    ratings = []
    for rating in ratings_list:
        ratings.append(rating[0])

    if len(ratings)>0:
        avg_rating = round(sum(ratings)/len(ratings), 2)
    else:
        avg_rating = None

    sql_update = text("UPDATE restaurants SET avg_rating = :avg_rating WHERE id = :restaurant_id;")
    db.session.execute(sql_update, {"avg_rating": avg_rating, "restaurant_id": restaurant_id})
    db.session.commit()

    return avg_rating

def list_reviews(restaurant_id):
    sql = text("SELECT user_id, rating, comment FROM reviews WHERE restaurant_id = :restaurant_id;")
    result = db.session.execute(sql, {"restaurant_id": restaurant_id})
    reviews = list(result.fetchall())

    review_list = []

    for review in reviews:
        id = review[0]
        sql_username = text("SELECT username FROM users WHERE id = :id")
        u_name = db.session.execute(sql_username, {"id": id}).fetchone()[0]
        review_list.append({"username": u_name, "rating": review[1], "comment": review[2]})

    return review_list


def delete_review():
    #only if admin
    pass
