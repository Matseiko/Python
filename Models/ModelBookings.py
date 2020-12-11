from Database import db
from marshmallow import Schema, fields, validate, ValidationError

class Bookings(db.Model):

    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users', backref='users')
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    car = db.relationship('Cars', backref='cars', uselist=False)
    booking_from = db.Column(db.DateTime, nullable=False)
    booking_until = db.Column(db.DateTime, nullable=False)

    def __init__(self, user=None, car=None, booking_from=None, booking_until=None):
        self.user = user
        self.car = car
        self.booking_from = booking_from
        self.booking_until = booking_until

    def read_from_db(self, booking_id):
        read_booking = Bookings.query.filter_by().all()
        self.user = read_booking.user
        self.car = read_booking.car
        self.booking_from = read_booking.booking_from
        self.booking_until = read_booking.booking_until


class BookingSchema(Schema):
    #user_id = fields.Str(required=True)
    #car_id = fields.Str(required=True)
    booking_from = fields.Str(required=True)
    booking_until = fields.Str(required=True)

