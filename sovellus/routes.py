from app import app
from flask import redirect, render_template, request, session, flash
from users import login, register, logout
from restaurants import get_all_restaurants, search_restaurant, add_restaurant, delete_restaurant

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

@app.route("/")
def add_restaurant_route():
    pass

@app.route("/search")
def search_route():
    #ender_template("search.html")
    pass