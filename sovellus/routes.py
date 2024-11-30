from app import app
from flask import redirect, render_template, request, session, flash
from users import login, register, logout, become_admin, is_admin
from restaurants import get_all_restaurants, add_restaurant, delete_restaurant, show_restaurant, search_restaurant
from groups import get_all_groups, add_group, add_restaurant_to_group
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
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            flash("Salasanat eroavat.")
            return redirect("/register")
        
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
        address = request.form["address"]
        opening_hours = request.form["openinghours"]
        info = request.form["info"]
        type = request.form["type"]
        avg_rating = 0
        restaurant_id = add_restaurant(name, address, opening_hours, info, avg_rating, type)
        if add_restaurant(name, address, opening_hours, info, avg_rating, type):
            flash("Ravintolan lisääminen onnistui!")
            return redirect("/restaurant/"+str(restaurant_id))
        else:
            flash("Ravintolan lisääminen ei onnistunut")

@app.route("/restaurant/<int:restaurant_id>")
def restaurant_info_route(restaurant_id):
    information = show_restaurant(restaurant_id)
    return render_template("restaurant_page.html", id = restaurant_id, name = information[0][1], openinghours = information[0][2], address = information[0][3], info = information[0][4], avg_rating = information[0][6], type = information[0][7], reviews = list_reviews(restaurant_id))

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
        comment = request.form["comment"]
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
        if add_group(name):
            flash("Ryhmä lisätty")
            return redirect("/add_group/"+str(restaurant_id))
        else:
            flash("Ryhmää ei voitu lisätä")