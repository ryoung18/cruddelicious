from flask import render_template, Blueprint

skus_blueprint = Blueprint(
  'skus',
  __name__,
  template_folder='templates'
)

@skus_blueprint.route('/')
def index(description_id):
  return render_template('skus/index.html')

@skus_blueprint.route('/new')
def new():
  return render_template('skus/new.html')


@skus_blueprint.route('/<int:id>/edit')
def edit(id):
  return render_template('skus/edit.html')
