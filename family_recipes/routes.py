from flask import render_template
from family_recipes import app, db
from family_recipes.models import Diet, Recipe


@app.route("/")
def home():
    return render_template("base.html")