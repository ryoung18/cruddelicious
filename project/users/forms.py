from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
  email = StringField('E-mail', [validators.Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  firstname = StringField('First Name', [validators.Length(min=1)])
  lastname = StringField('Last Name', [validators.Length(min=1)])


class UserLogin(FlaskForm):
  email = StringField('E-mail', [validators.Length(min=3)])
  password = PasswordField('Password', validators=[DataRequired()])