from flask import request, render_template, session
from db import db
from sqlalchemy.sql import text

def add_group(name):
    creator_id = session["user_id"]
    sql = text("INSERT INTO groups (name, creator_id) VALUES (:name, :creator_id)")
    db.session.execute(sql, {"name": name, "creator_id": creator_id})
    db.session.commit()

    sql2 = text("SELECT id FROM groups WHERE name LIKE :name")
    group_id = db.session.execute(sql2, {"name": name}).fetchone()
    
    return group_id[0]

def get_all_groups():
    sql = text("SELECT id, name FROM groups ORDER BY name")
    return db.session.execute(sql).fetchall()

def get_restaurants_groups(restaurant_id):
    sql = text("SELECT group_id FROM map_group WHERE restaurant_id = :restaurant_id")
    groups = db.session.execute(sql, {"restaurant_id": restaurant_id}).fetchall()
    names = []
    for group in groups:
        group_id = group[0]
        sql_name = text("SELECT name FROM groups WHERE id = :group_id")
        name = db.session.execute(sql_name, {"group_id": group_id}).fetchone()[0]
        names.append({"name": name})

    return names

def get_groups_restaurants(group_id):
    sql = text("SELECT restaurant_id FROM map_group WHERE group_id = :group_id")
    restaurants = db.session.execute(sql, {"group_id": group_id}).fetchall()
    names = []
    for restaurant in restaurants:
        restaurant_id = restaurant[0]
        sql_name = text("SELECT name FROM restaurants WHERE id = :restaurant_id")
        name = db.session.execute(sql_name, {"restaurant_id": restaurant_id}).fetchone()[0]
        names.append({"name": name})

    return names

def add_restaurant_to_group(restaurant_id, group_id):
    sql = text("INSERT INTO map_group (restaurant_id, group_id) VALUES (:restaurant_id, :group_id)")
    db.session.execute(sql, {"restaurant_id": restaurant_id, "group_id": group_id})
    db.session.commit()
    return True

def get_groups_name(group_id):
    sql = text("SELECT name FROM groups WHERE id = :id")
    group_name_row = db.session.execute(sql, {"id": group_id}).fetchone()
    group_name = group_name_row[0]
    return group_name
    
def delete_group(group_id):
    sql = text("UPDATE groups SET visible=0 WHERE id = :group_id;")
    db.session.execute(sql, {"group_id": group_id})
    db.session.commit()
    return True