from flask import request, render_template
from db import db
from sqlalchemy.sql import text

def search_restaurant():
    query = request.args["query"]
    sql = text("SELECT id, content FROM restaurants WHERE info LIKE "%query%";")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    restaurants = result.fetchall()
    return render_template("search.html", restaurants=restaurants)

def get_all_restaurants():
    sql = text("SELECT id, name FROM restaurants WHERE visible = TRUE ORDER BY name")
    a = db.session.execute(sql).fetchall()
    return db.session.execute(sql).fetchall()


# only administrator

def add_restaurant():
    #check if admin
    name = request.form["name"]
    openinghours = request.form["openinghours"]
    address = request.form["address"]
    info = request.form["info"]
    #r_type = request.form["type"]

    #add rating
    #sql_r = text("SELECT rating FROM reviews WHERE restaurant_id = name")
    #result = db.session.execute(sql_r, {"name":name})
    #ratings = list(result.fetchall())
    #avg = sum(ratings)/len(ratings)

    sql = text("INSERT INTO restaurants (name, openinghours, address, info, visible) VALUES (:name, :openinghours, :address, :info, :visible)")
    db.session.execute(sql, {"name": name, "openinghours": openinghours, "address": address, "info": info, "visible": 1})
    return db.session.commit()

def delete_restaurant():
    #check if admin
    name = request.form["name"]

    sql = text("UPDATE restaurants SET visible=0 WHERE name LIKE :name;")
    db.session.execute(sql, {"name": name})
    return db.session.commit()

