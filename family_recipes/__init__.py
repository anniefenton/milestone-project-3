import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from family_recipes import routes  # noqa

