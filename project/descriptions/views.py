from flask import render_template, Blueprint
from project.models import Description
from flask_login import login_required

descriptions_blueprint = Blueprint(
    'descriptions',
    __name__,
    template_folder='templates'
)

@descriptions_blueprint.route('/')
# @login_required
def index():
  return render_template('descriptions/index.html', descriptions = Description.query.all())

@descriptions_blueprint.route('/new')
# @login_required
def new():
  return render_template('descriptions/new.html')



