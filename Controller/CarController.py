from Models.ModelCars import Cars, CarSchema
from Models.ModelUsers import Users
from marshmallow import ValidationError
from flask import jsonify
from Database import db

class CarController(object):

    def create(self, car_data=None):
        name = car_data.get('name')
        price = car_data.get('price')

        car = Cars(name, price)

        try:
            result = CarSchema().load(car_data)
        except ValidationError as err:
            return jsonify(message="Error", status=400)

        if name and price:
            db.session.add(car)
            db.session.commit()
            return jsonify(message="The car is created !", status=200)
        else:
            return jsonify(message="Missing values !", status=404)

    def read(self, car_id=None):
        car = Cars.query.filter_by(id=car_id).first()
        if car is None:
            return jsonify(message="The car was not found", status=404)
        else:
            #car.read_from_db(car_id)
            return jsonify({'Name': car.name, 'price': car.price, 'status': 200})

    def read_all(self, car_id=None):
        return Cars.query.filter_by().all()

    def update_car(self, car_id=None, car_data=None):
        new_price = car_data.get('new_price')
        car = Cars.query.filter_by(id=car_id).first()
        user_id = car_data.get('user_id')
        user = Users.query.filter_by(id=user_id).first()

        if new_price:
            car.price = new_price
            db.session.add(car)
            db.session.commit()
            return jsonify(message="Car was updated !", status=200)
        else:
            return jsonify(message="Missing values !", status=404)

    def delete(self, car_id=None, user_id=None):
        car = Cars.query.filter_by(id=car_id).first()
        user = Users.query.filter_by(id=user_id).first()
        if user.role == 'passenger':
            return jsonify(message="You do not have access !", status=403)
        if car is None:
            return jsonify(message="The car was not found !", status=404)
        else:
            car.delete_from_db(car_id)
            return jsonify(message="Car was deleted !", status=200)


