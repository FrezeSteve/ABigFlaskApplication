from myproject.core.views import core
from myproject.error_pages.handlers import error_pages
from myproject.users.views import users
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.register_blueprint(error_pages)
app.register_blueprint(core)
app.register_blueprint(users)


# DATABASE
basedir = os.path.dirname(__file__)

# the various configurations of the application
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db definations
db = SQLAlchemy(app)
Migrate(app, db)

# Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
