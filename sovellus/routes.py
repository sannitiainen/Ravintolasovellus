from app import app
from flask import redirect, render_template, request, session, flash
from users import login, register, logout, become_admin, is_admin
from restaurants import get_all_restaurants, add_restaurant, delete_restaurant, show_restaurant, search_restaurant
from groups import get_all_groups, add_group, add_restaurant_to_group, get_restaurants_groups
from reviews import add_review, list_reviews

# home page
@app.route("/")
def index():
    query = request.args.get("query")
    if query:
        results = search_restaurant(query)
    else:
        results = []
    return render_template("index.html", restaurants = get_all_restaurants(), search_results = results, query = query)

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
        if len(username) < 5 or len(username) > 15:
            flash("Käyttäjätunnnuksen tulee olla 5-15 merkkiä pitkä")
        
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            flash("Salasanat eroavat.")
        if len(password1)< 5:
            flash("Salasanan tulee olla yli 5 merkkiä pitkä")
            
        
        if not register(username, password1):
            flash("Rekisteröinti ei onnistunut")
            return redirect("/register")

        else:
            flash("Rekisteröinti onnistui!")
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
        name = request.form["name"]
        if len(name)<1:
            flash("Anna ravintolalle nimi")
        if len(name)>30:
            flash("Nimi on liian pitkä")

        address = request.form["address"]
        if address == "":
            address = "ei tietoa"
        if len(address) > 30:
            flash("Osoite saa olla korkeintaan 30 merkkiä")

        opening_hours = request.form["openinghours"]
        if opening_hours == "":
            opening_hours = "ei tietoa"
        if len(opening_hours) > 50:
            flash("Aukioloajassa saa olla korkeintaan 50 merkkiä")

        info = request.form["info"]
        if info == "":
            info = "-"
        if len(info) > 1000:
            flash("Info saa olla korkeintaan 1000 merkkiä")

        type = request.form["type"]
        if type == "":
            type = "ei tietoa"

        avg_rating = 0
        restaurant_id = add_restaurant(name, address, opening_hours, info, avg_rating, type)
        if restaurant_id:
            flash("Ravintolan lisääminen onnistui!")
            return redirect("/restaurant/"+str(restaurant_id))
        else:
            flash("Ravintolan lisääminen ei onnistunut")

@app.route("/restaurant/<int:restaurant_id>")
def restaurant_info_route(restaurant_id):
    information = show_restaurant(restaurant_id)
    return render_template("restaurant_page.html", id = restaurant_id, name = information[0][1], openinghours = information[0][2], address = information[0][3], info = information[0][4], avg_rating = information[0][6], type = information[0][7], reviews = list_reviews(restaurant_id), groups = get_restaurants_groups(restaurant_id))

@app.route("/restaurant/<int:restaurant_id>", methods = ["GET", "POST"])
#MUUTA TÄTÄ!!
def add_review_route(restaurant_id):
    if "user_id" not in session:
        flash("Kirjaudu sisään")
        return redirect("/login")
    if request.method == "GET":
        return render_template("restaurant_page.html")
    if request.method == "POST":

        rating = request.form["rating"]
        if rating > 5:
            flash("Varmista että arvio on välillä 1-5")

        comment = request.form["comment"]
        if len(comment) < 1:
            comment = "ei kommenttia"

        user_id = session["user_id"]
        restaurant_id = restaurant_id
        if add_review(user_id, restaurant_id, rating, comment):
            flash("Arvion lisääminen onnistui!")
            return redirect("/restaurant/"+str(restaurant_id))
        else: 
            flash("Arvion lisääminen ei onnistunut")

@app.route("/delete_restaurant/<int:restaurant_id>", methods = ["GET", "POST"])
def delete_restaurant_route(restaurant_id):
    if delete_restaurant(restaurant_id):
        flash("Ravintola poistettu")
        return redirect("/")
    else:
        flash("Ravintolaa ei voitu poistaa.")
        return redirect("/restaurant/"+str(restaurant_id))



@app.route("/become_admin", methods = ["GET", "POST"])
def become_admin_route():
    if request.method == "GET":
        return render_template("become_admin.html")
    
    if request.method == "POST":
        if become_admin():
            flash("Olet nyt ylläpitäjä")
            return redirect("/")
        else:
            flash("Jokin meni vikaan")

@app.route("/add_group/<int:restaurant_id>", methods = ["GET", "POST"])
def add_restaurant_to_group_route(restaurant_id):
    if request.method == "GET":
        return render_template("groups.html", restaurant_id=restaurant_id, groups = get_all_groups())
    if request.method == "POST":
        group_ids = request.form.getlist("group_ids")
        for group_id in group_ids:
            if add_restaurant_to_group(restaurant_id, group_id):
                flash("Ravintola lisätty valittuihin ryhmiin")
            else:
                flash("Ravintolaa ei lisätty mihinkään ryhmään")
        return redirect("/restaurant/"+str(restaurant_id))
                

@app.route("/add_new_group/<int:restaurant_id>", methods = ["GET", "POST"])
def add_group_route(restaurant_id):
    if request.method == "GET":
        return render_template("add_group.html", restaurant_id=restaurant_id)
    if request.method == "POST":
        name = request.form["name"]

        if len(name)<1:
            flash("Anna ryhmälle nimi")
        if len(name)>30:
            flash("Nimi on liian pitkä")
            return redirect("/add_group/"+str(restaurant_id))

        if add_group(name):
            flash("Ryhmä lisätty")
            return redirect("/add_group/"+str(restaurant_id))
        else:
            flash("Ryhmää ei voitu lisätä")