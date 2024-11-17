from flask import request, render_template
from db import db

def search_restaurant():
    query = request.args["query"]
    sql = "SELECT id, content FROM restaurants WHERE info LIKE "%query%";"
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    messages = result.fetchall()
    return render_template("result.html", messages=messages)


# only administrator
def add_restaurant():
    #check if admin
    name = request.form["name"]
    openinghours = request.form["openinghours"]
    address = request.form["address"]
    info = request.form["info"]

    sql = "INSERT INTO restaurants (name, openinghours, address, info, visible) VALUES (:name, :openinghours, :address, :info, :visible)"
    db.session.execute(sql, {"name": name, "openinghours": openinghours, "address": address, "info": info, "visible": True})
    db.session.commit()

def delete_restaurant():
    #check if admin
    name = request.form["name"]

    sql = "UPDATE restaurants SET visible=FALSE WHERE name LIKE :name;"
    db.session.execute(sql, {"name": name})
    db.session.commit()

