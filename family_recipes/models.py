from family_recipes import db

class Diet(db.Model):
    # schema for the Diet model
    id = db.Column(db.Integer, primary_key=True)
    diet_type = db.Column(db.String(30), unique=True, nullable=False)
    recipes = db.relationship("Recipe", backref="diet", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent self as a string
        return self.diet_type


class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(60), unique=True, nullable=False)
    family_member = db.Column(db.String(30), nullable=False)
    time_to_make = db.Column(db.Time, nullable=False)
    serving_size = db.Column(db.Integer, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    method = db.Column(db.Text, nullable=False)
    diet_id = db.Column(db.Integer, db.ForeignKey("diet.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent self as a string
        return f"#{self.id} - Recipe:{self.recipe_name} | Family Member: {self.family_member}"