from app import app
from flask import redirect, render_template, request, session, flash
from users import login, register, logout
from restaurants import get_all_restaurants, search_restaurant, add_restaurant, delete_restaurant

# home page
@app.route("/")
def index():
    return render_template("index.html", restaurants = get_all_restaurants())

# login/register

@app.route("/login", methods=["GET", "POST"])
def login_route():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if login(username, password):
            return redirect("/")
        else:
            flash("Väärä tunnus tai salasana")
            return redirect("/login")

@app.route("/register", methods = ["GET", "POST"])
def register_route():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            flash("Salasanat eroavat.")
            return redirect("/register")
        
        if not register(username, password1):
            flash("Rekisteröinti ei onnistunut")
            return redirect("/register")

        else:
            flash("Rekisteröinti onnistui! Kirjaudu sisään.")
            return redirect("/")


@app.route("/logout")
def logout_route():
    logout()
    return redirect("/")

# restaurants

@app.route("/add_restaurant", methods=["GET", "POST"])
def add_restaurant_route():
    if request.method == "GET":
        return render_template("add_restaurant.html")
    if request.method == "POST":
        print("ok")
        name = request.form["name"]
        address = request.form["address"]
        opening_hours = request.form["openinghours"]
        info = request.form["info"]
        type = request.form["type"]
        restaurant_id = add_restaurant(name, address, opening_hours, info, type)
        if add_restaurant(name, address, opening_hours, info, type):
            flash("Ravintolan lisääminen onnistui!")
            return redirect("/restaurant/"+str(restaurant_id))
        else:
            print("paske")


@app.route("/search", methods = ["GET"])
def search_route():
    #ender_template("search.html")
    pass