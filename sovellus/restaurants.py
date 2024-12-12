from flask import request, render_template, session
from db import db
from sqlalchemy.sql import text

def search_restaurant(query):
    sql = text("SELECT id, name FROM restaurants WHERE info LIKE :query;")
    return db.session.execute(sql, {"query": f"%{query}%"}).fetchall()

def get_all_restaurants():
    sql = text("SELECT id, name FROM restaurants WHERE visible = 1 ORDER BY avg_rating, name")
    return db.session.execute(sql).fetchall()


# only administrator

def add_restaurant(name, address, openinghours, info, avg_rating, type):
    sql = text("INSERT INTO restaurants (name, openinghours, address, info, visible, avg_rating, type) VALUES (:name, :openinghours, :address, :info, :visible, :avg_rating, :type);")
    db.session.execute(sql, {"name": name, "openinghours": openinghours, "address": address, "info": info, "visible": 1, "avg_rating": avg_rating, "type":type})
    db.session.commit()

    sql2 = text("SELECT id FROM restaurants WHERE name LIKE :name")
    restaurant_id_row = db.session.execute(sql2, {"name": name}).fetchone()
    restaurant_id = restaurant_id_row[0]

    return restaurant_id

def show_restaurant(restaurant_id):
    sql = text("SELECT * FROM restaurants WHERE id = :id")
    restaurant = db.session.execute(sql, {"id": restaurant_id}).fetchall()
    return restaurant

def modify_information(restaurant_id, address, opening_hours, info, type):
    sql = text("UPDATE restaurants SET address = :address, openinghours = :openinghours, info = :info, type = :type WHERE id = :id")
    db.session.execute(sql, {"address": address, "openinghours": opening_hours, "info": info,"type": type,"id": restaurant_id})
    db.session.commit()
    return True

def get_name(restaurant_id):
    sql2 = text("SELECT name FROM restaurants WHERE id = :id")
    restaurant_name_row = db.session.execute(sql2, {"id": restaurant_id}).fetchone()
    restaurant_name = restaurant_name_row[0]
    return restaurant_name

def delete_restaurant(restaurant_id):
    sql = text("UPDATE restaurants SET visible=0 WHERE id = :restaurant_id;")
    db.session.execute(sql, {"restaurant_id": restaurant_id})
    db.session.commit()
    return True #MYÖS FALSE VAIHTOEHTO!!




