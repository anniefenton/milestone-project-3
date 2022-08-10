from flask import render_template
from family_recipes import app, db


@app.route("/")
def home():
    return render_template("base.html")