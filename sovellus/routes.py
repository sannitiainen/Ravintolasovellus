from app import app
from flask import redirect, render_template, request, session, flash
from users import login

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login_route():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        login(username, password)


@app.route("/register")
def register_route():
    return render_template("register.html")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

