from family_recipes import db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


class User(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        # __repr__ to represent self as a string
        return self.diet_type


class Diet(db.Model):
    # schema for the Diet model
    id = db.Column(db.Integer, primary_key=True)
    diet_type = db.Column(db.String(30), unique=True, nullable=False)
    recipes = db.relationship(
        "Recipe", backref="diet", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent self as a string
        return self.diet_type


class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(60), unique=True, nullable=False)
    family_member = db.Column(db.String(30))
    time_to_make = db.Column(db.Integer, nullable=False)
    serving_size = db.Column(db.Integer, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    method = db.Column(db.Text, nullable=False)
    diet_id = db.Column(
        db.Integer, db.ForeignKey("diet.id", ondelete="CASCADE"))

    def __repr__(self):
        # __repr__ to represent self as a string
        return f"#{self.id} - Recipe:{self.recipe_name} | Family Member: {self.family_member}"
