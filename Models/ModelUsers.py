from Database import db
from marshmallow import Schema, fields
from app import manager


class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    role = db.Column(db.String, nullable=False)


    def __init__(self, email=None, password=None, first_name=None,
                 last_name=None, birthday=None, role=None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.role = role

    def add_user_to_db(self):
        data = Users(self.email, self.password, self.first_name,
                     self.last_name, self.birthday, self.role)

    def read_from_db(self, user_id):
        read_user = Users.query.filter_by(id=user_id).first()
        self.first_name = read_user.first_name
        self.last_name = read_user.last_name
        self.birthday = read_user.birthday
        self.role = read_user.role

    def delete_from_db(self, user_id):
        delete_user = Users.query.filter_by(id=user_id).first()
        db.session.delete(delete_user)
        db.session.commit()


class UserSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    birthday = fields.Str(required=True)
    role = fields.Str(required=True)


@manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)