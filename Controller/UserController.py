from Models.ModelUsers import Users, UserSchema
from marshmallow import ValidationError
from flask import jsonify
from Database import db, bcrypt
import datetime


class UserController(object):

    def create(self, user_data=None):
        email = user_data.get('email')
        password = user_data.get('password')
        pw_hash = bcrypt.generate_password_hash('password')
        first_name = user_data.get('first_name')
        last_name = user_data.get('last_name')
        birthday = user_data.get('birthday')
        role = user_data.get('role')
        birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
        user = Users(email, pw_hash, first_name, last_name, birthday_date, role)

        try:
            result = UserSchema().load(user_data)
        except ValidationError as err:
            return jsonify(message="Error!", status=400)

        if email and password and first_name and last_name and birthday and role:
            db.session.add(user)
            db.session.commit()
            return jsonify(message="The user is created !", status=200)
        else:
            return jsonify(message="Missing values !", status=404)

    def read(self, user_id=None):
        user = Users.query.filter_by(id=user_id).first()
        #car = Cars()
        if user is None:
            return jsonify(message="The user was not found !", status=404)
        else:
            #car.read_from_db(car_id)
            return jsonify({'   first_name': user.first_name, '   last name':  user.last_name, '   birthday': user.birthday,'   role': user.role, '   status': 200})

    def delete(self, user_id=None):
        user = Users.query.filter_by(id=user_id).first()
        if user is None:
            return jsonify(message="The user was not found !", status=404)
        else:
            user.delete_from_db(user_id)
            return jsonify(message="User was deleted !", status=200)
