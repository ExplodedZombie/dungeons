from flask import Flask, redirect, url_for, g
from flask_modus  import Modus
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from project.users.forms import UserLoginForm
import os


app = Flask(__name__)

# If we are in production, make sure we DO NOT use the debug mode
if os.environ.get('ENV') == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# allows user to use their session
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

csrf = CSRFProtect(app)
modus = Modus(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
# redirect the user if they try to access a private route
login_manager.login_view = "users.login"
login_manager.login_message = "Please log in."
login_manager.login_message_category = "alert-warning"

# import and register blueprints for our resources
from project.home.views import home_blueprint
app.register_blueprint(home_blueprint, url_prefix='/home')

from project.users.views import users_blueprint
app.register_blueprint(users_blueprint, url_prefix='/users')

from project.games.views import games_blueprint
app.register_blueprint(games_blueprint, url_prefix='/games')

@app.route('/')
def root():
    return redirect(url_for('home.index'))

from project.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_request
def login_form():
    if not current_user.is_authenticated:
        g.login_form = UserLoginForm()
