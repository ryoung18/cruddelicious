from project import db,bcrypt
from flask_login import UserMixin


class User(db.Model, UserMixin):
  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.Text, unique=True)
  password = db.Column(db.Text)
  firstname = db.Column(db.Text)
  lastname = db.Column(db.Text)


  def __init__(self, email, password, firstname, lastname):
    self.email = email
    self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
    self.firstname = firstname
    self.lastname = lastname

  @classmethod
  def authenticate(cls, email, password):
    found_user = cls.query.filter_by(email = email).first()
    if found_user:
        authenticated_user = bcrypt.check_password_hash(found_user.password, password)
        if authenticated_user:
            return found_user
    return False

    def __repr__(self):
      return "Username {} Password hidden".format(self.email)


class Description(db.Model):
  __tablename__ = "descriptions"

  id = db.Column(db.Integer, primary_key=True)
  name  = db.Column(db.Text)
  description = db.Column(db.Text)
  skus = db.relationship('Sku', backref='description', lazy='dynamic', cascade='delete')

  def __init__(self, name, description):
    self.name = name
    self.description = description

  def __repr__(self):
    return "The description is ' {} ' ".format(self.description)

class Sku(db.Model):
  __tablename__ = "skus"

  id = db.Column(db.Integer, primary_key=True)
  sku = db.Column(db.Text)
  description_id = db.Column(db.Integer, db.ForeignKey('descriptions.id'))
  size = db.Column(db.Text)
  color = db.Column(db.Text)
  img = db.Column(db.Text)
  inventories = db.relationship('Inventory', backref='sku', lazy='dynamic')
  transactions = db.relationship('Transaction', backref='sku', lazy='dynamic')

  def __init__(self, sku, description_id, size, color, img):
    self.sku = sku
    self.description_id = description_id
    self.size = size
    self.color = color
    self.img = img


  def __repr__(self):
    return "The sku is ' {} ', descr id is {}, size {}, color {}, img {}".format(self.sku, self.description_id, self.size, self.color, self.img)

class Transaction(db.Model):
  __tablename__ = "transactions"

  id = db.Column(db.Integer, primary_key=True)
  sku_id = db.Column(db.Integer, db.ForeignKey('skus.id'))
  date = db.Column(db.DateTime)
  qty = db.Column(db.Integer)
  type  = db.Column(db.Text)
  description = db.Column(db.Text)
  amount = db.Column(db.Float)
  shipping_cost = db.Column(db.Float)
  shipping_method = db.Column(db.Text)


  def __init__(self, sku_id, date, qty, type, description, amount, shipping_cost, shipping_method):
    self.sku_id = sku_id
    self.date = date
    self.qty = qty
    self.type = type
    self.description = description
    self.amount = amount
    self.shipping_cost = shipping_cost
    self.shipping_method = shipping_method

  def __repr__(self):
    return "sku_id {}, date {}, qty {}, type {}, desc {}, amount {} shipping cost {} shipping method {}".format(self.sku_id, self.date, self.qty, self.type, self.description, self.amount, self.shipping_cost, self.shipping_method)

class Inventory(db.Model):
  __tablename__ = "inventories"

  id = db.Column(db.Integer, primary_key=True)
  sku_id = db.Column(db.Integer, db.ForeignKey('skus.id'))
  amount = db.Column(db.Float)
  date = db.Column(db.DateTime)
  qty = db.Column(db.Integer)

  def __init__(self, sku_id, date, amount, qty):
    self.sku_id = sku_id
    self.date = date
    self.amount = amount
    self.qty = qty

  def __repr__(self):
    return "The sku id ' {} ', date {}, amount {}, qty {}".format(self.sku_id, self.date, self.amount, self.qty)