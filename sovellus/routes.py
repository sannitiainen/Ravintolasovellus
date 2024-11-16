from app import app
from flask import redirect, render_template, request, session, flash

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/register")
def register_route():
    return render_template("register.html")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
