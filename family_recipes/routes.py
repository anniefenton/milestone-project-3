from flask import render_template
from family_recipes import app, db
from family_recipes.models import Diet, Recipe


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/recipes")
def recipes():
    return render_template("recipes.html")