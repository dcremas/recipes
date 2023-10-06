from configparser import ConfigParser
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

config = ConfigParser()
config.read("config.ini")

username = config["RECIPE_DB"]["username"]
password = config["RECIPE_DB"]["password"]
host = config["RECIPE_DB"]["host"]
port = config["RECIPE_DB"]["port"]
database = config["RECIPE_DB"]["database"]

app = Flask(__name__)
app.config["SECRET_KEY"] = "422dd133ac637d5fbe9d690b058bc119"
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@{host}:{port}/{database}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = SQLAlchemy()
db.init_app(app)

import routes, models
