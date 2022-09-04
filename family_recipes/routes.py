from flask import render_template, request, url_for, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from family_recipes import app, db
from family_recipes.models import User, Diet, Recipe


@app.route("/")
def home():
    return render_template("home.html")


# Recipes
@app.route("/recipe")
def recipe():
    recipe = list(Recipe.query.order_by(Recipe.id).all())
    return render_template("recipe.html", recipes=recipe)


# Add recipes
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    diet = list(Diet.query.order_by(Diet.diet_type).all())
    if request.method == "POST":
        recipe = Recipe(
            recipe_name=request.form.get("recipe_name"),
            family_member=request.form.get("family_member"),
            time_to_make=request.form.get("time_to_make"),
            serving_size=request.form.get("serving_size"),
            ingredients=request.form.get("ingredients"),
            method=request.form.get("method"),
            diet_id=request.form.get("diet")
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("recipe"))
    return render_template("add_recipe.html", diets=diet)


# Edit recipes
@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    diet = list(Diet.query.order_by(Diet.diet_type).all())
    if request.method == "POST":
        recipe.recipe_name = request.form.get("recipe_name")
        recipe.family_member = request.form.get("family_name")
        recipe.time_to_make = request.form.get("time_to_make")
        recipe.serving_size = request.form.get("serving_size")
        recipe.ingredients = request.form.get("ingredients")
        recipe.method = request.form.get("method")
        recipe.diet_id = request.form.get("diet_id")
        db.session.commit()
        return redirect(url_for("recipe"))
    return render_template("edit_recipe.html", recipe=recipe, diets=diet)


# Delete Recipes
@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("recipe"))


# Diet
@app.route("/diet")
def diet():
    diet = list(Diet.query.order_by(Diet.diet_type).all())
    return render_template("diet.html", diets=diet)


# Add Diets
@app.route("/add_diet", methods=["GET", "POST"])
def add_diet():
    if request.method == "POST":
        diet = Diet(diet_type=request.form.get("diet_type"))
        db.session.add(diet)
        db.session.commit()
        return redirect(url_for("diet"))
    return render_template("add_diet.html")


#Edit Diet
@app.route("/edit_diet/<int:diet_id>", methods=["GET", "POST"])
def edit_diet(diet_id):
    diet = Diet.query.get_or_404(diet_id)
    if request.method == "POST":
        diet.diet_type = request.form.get("diet_type")
        db.session.commit()
        return redirect(url_for("diet"))
    return render_template("edit_diet.html", diet=diet)


# Delete Diet
@app.route("/delete_diet/<int:diet_id>")
def delete_diet(diet_id):
    diet = Diet.query.get_or_404(diet_id)
    db.session.delete(diet)
    db.session.commit()
    return redirect(url_for("diet"))
