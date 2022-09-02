from flask import render_template, request, url_for, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from family_recipes import app, db
from family_recipes.models import User, Diet, Recipe


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        existing_user = User.query.filter(
            User.username == request.form.get("username").lower()).all()

        if existing_user:
            flash("This username already exists")
            return redirect(url_for("register"))
            
        new_user = User(
            username=request.form.get("username").lower(),
            email=request.form.get("email").lower(),
            password=generate_password_hash(request.form.get("password")),
        )

        test_pass = generate_password_hash(request.form.get("password"))
        print(f"Pass: {test_pass}")
        print(f"Length: {len(test_pass)}")

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!')
        return redirect(url_for('login'))

    return render_template("register.html")

@app.route("/recipes")
def recipes():
    return render_template("recipes.html")