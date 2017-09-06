from flask import render_template, Blueprint
from flask_login import login_required

inventories_blueprint = Blueprint(
    'inventories',
    __name__,
    template_folder='templates'
)

@inventories_blueprint.route('/')
@login_required
def index():
  return render_template('inventories/index.html')

@inventories_blueprint.route('/new')
@login_required
def new():
  return render_template('inventories/new.html')



