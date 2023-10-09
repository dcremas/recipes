from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

external_url = "postgresql://dustincremascoli:2J6oodf6lY1xEgssydxTR1Pb9QPNFBuj@dpg-cki06rcldqrs73f2cgng-a.ohio-postgres.render.com/recipe_y6ux"

app = Flask(__name__)
app.config["SECRET_KEY"] = "422dd133ac637d5fbe9d690b058bc119"
app.config["SQLALCHEMY_DATABASE_URI"] = external_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = SQLAlchemy()
db.init_app(app)

import routes, models
