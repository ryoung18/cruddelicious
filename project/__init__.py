from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_login import current_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/warehouse_sales'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bcrypt = Bcrypt(app)
modus = Modus(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
login_manager.login_message = ''


from project.models import User

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)


from project.users.views import users_blueprint
app.register_blueprint(users_blueprint, url_prefix='/users')

from project.descriptions.views import descriptions_blueprint
app.register_blueprint(descriptions_blueprint, url_prefix='/descriptions')

from project.skus.views import skus_blueprint
app.register_blueprint(skus_blueprint, url_prefix='/descriptions/<int:description_id>/skus')

from project.transactions.views import transactions_blueprint
app.register_blueprint(transactions_blueprint, url_prefix='/descriptions/<int:description_id>/skus/<int:sku_id>/transactions')

from project.inventories.views import inventories_blueprint
app.register_blueprint(inventories_blueprint, url_prefix='/<int:sku_id>/inventories')

@app.route('/')
def root():
  if(current_user.is_authenticated):
      return render_template('users/index.html')
  return redirect(url_for('users.index'))