from Models.ModelBookings import Bookings, BookingSchema
from Models.ModelUsers import Users
from Models.ModelCars import Cars
from marshmallow import ValidationError
from flask import jsonify
from Database import db
from re import *
import datetime

class BookingController(object):

    def create(self, booking_data=None, user_id=None, car_id=None):
        booking_from = booking_data.get('booking_from')
        booking_until = booking_data.get('booking_until')
        date_type = compile('(^|\s)(\d){4}(\-)(\d){2}(\-)(\d){2}(\s|$)')
        if not date_type.match(booking_from) or not date_type.match(booking_until):
            return jsonify(message="ERROR", status=400)
        booking_from_date = datetime.datetime.strptime(booking_from, "%Y-%m-%d").date()
        booking_until_date = datetime.datetime.strptime(booking_until, "%Y-%m-%d").date()
        user = Users.query.filter_by(id=user_id).first()
        car = Cars.query.filter_by(id=car_id).first()
        booking = Bookings(user, car, booking_from_date, booking_until_date)


        try:
            result = BookingSchema().load(booking_data)
        except ValidationError as err:
            return jsonify(message="ERROR", status=400)
            #return err.messages

        if user and car and booking_from and booking_until:
            db.session.add(car)
            db.session.commit()
            return jsonify(message="The booking is created !", status=200)

    def read(self, booking_id=None):
        return Bookings.query.filter_by().all()