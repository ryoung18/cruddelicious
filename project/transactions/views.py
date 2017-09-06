from flask import render_template, Blueprint
from flask_login import login_required

# import datetime
# datetime.datetime.now()

transactions_blueprint = Blueprint(
    'transactions',
    __name__,
    template_folder='templates'
)

@transactions_blueprint.route('/')
# @login_required
def index(description_id, sku_id):
  return render_template('transactions/index.html')

@transactions_blueprint.route('/new')
# @login_required
def new():
  return render_template('transactions/new.html')



