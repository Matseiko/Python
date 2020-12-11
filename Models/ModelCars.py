from Database import db
from marshmallow import Schema, fields, validate, ValidationError


class Cars(db.Model):

    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)


    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price

    def add_car_to_db(self):
        data = Cars(self.name, self.price)
        db.session.add(data)
        db.session.commit()

    def read_from_db(self, car_id):
        read_car = Cars.query.filter_by(id=car_id).first()
        self.name = read_car.name
        self.price = read_car.price

    def read_from_db_all(self, car_id):
        read_cars = Cars.query.filter_by().all()
        self.id =read_cars.id
        self.name = read_cars.name
        self.price = read_cars.price

    def update_db(self, car_id):
        update_car = Cars.query.filter_by(id=car_id).first()
        self.price = update_car.new_price

    def delete_from_db(self, car_id):
        delete_car = Cars.query.filter_by(id=car_id).first()
        db.session.delete(delete_car)
        db.session.commit()


class CarSchema(Schema):
    name = fields.Str(validate=validate.Length(max=30), required=True)
    price = fields.Float(required=True)
