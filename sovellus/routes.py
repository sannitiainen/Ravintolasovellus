from app import app
from flask import redirect, render_template, request, session, flash
from users import login, register, logout, become_admin, is_admin
from restaurants import get_all_restaurants, search_restaurant, add_restaurant, delete_restaurant, show_restaurant
from reviews import add_review

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
    if not is_admin():
        flash("Sinulla ei ole oikeuksia tähän toimintoon")
        return redirect("/")
    if request.method == "GET":
        return render_template("add_restaurant.html")
    if request.method == "POST":
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
            flash("Ravintolan lisääminen ei onnistunut")


@app.route("/search", methods = ["GET"])
def search_route():
    #render_template("search.html")
    pass

@app.route("/restaurant/<int:restaurant_id>")
def restaurant_info_route(restaurant_id):
    info = show_restaurant(restaurant_id)
    return render_template("restaurant_page.html", id = restaurant_id, name = info[0][1], address = info[0][3], openinghours = info[0][2], type = info[0][4])

@app.route("/restaurant/<int:restaurant_id>", methods = ["GET", "POST"])
def add_review_route(restaurant_id):
    if "user_id" not in session:
        flash("Kirjaudu sisään")
        return redirect("/login")
    if request.method == "GET":
        return render_template("restaurant_page.html")
    if request.method == "POST":
        name = request.form["name"]
        rating = request.form["rating"]
        comment = request.form["comment"]
        restaurant_id = add_review(name, rating, comment)
        if add_review(name, rating, comment):
            flash("Arvion lisääminen onnistui!")
            return redirect("/restaurant/"+{restaurant_id})
        else: 
            flash("Arvion lisääminen ei onnistunut")

@app.route("/become_admin", methods = ["GET", "POST"])
def become_admin_route():
    if "user_id" not in session:
        flash("Kirjaudu sisään")
        return redirect("/login")
    
    if request.method == "GET":
        return render_template("become_admin.html")
    
    if request.method == "POST":
        if become_admin():
            flash("Olet nyt ylläpitäjä")
            return redirect("/")
        else:
            flash("Jokin meni vikaan")