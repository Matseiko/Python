from flask import request, jsonify, make_response
from app import app
from Models.ModelUsers import Users
from Controller.UserController import UserController
from Controller.CarController import CarController
from Controller.BookingController import BookingController
from Database import bcrypt
import jwt
from datetime import datetime, timedelta
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message':  'Token is missing !'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = Users.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': token + ' Token is invalid !'}), 401
        return f(current_user, *args, **kwargs)
    return decorated


@app.route("/start")
def hello():
    return jsonify(message="Hello world !", status=200)


# link to try: http://127.0.0.1:5000/UserCreate?email=vika@gmail.com&password=11111&first_name=Vika&last_name=Oh&birthday=2002-07-08&role=admin


@app.route('/UserCreate', methods=['GET'])
def hello_user():
    user_data = request.args
    user_controller = UserController()
    return user_controller.create(user_data)


# link to try: http://127.0.0.1:5000/CarCreate?name=BMW&price=100


@app.route('/CarCreate', methods=['GET'])
@token_required
def hello_car(current_user):
    if current_user.role != 'admin':
        return jsonify({'message': 'Cannot perform that function!'})
    car_data = request.args
    car_controller = CarController()
    if car_controller.create(car_data):
        return "Success!"
    else:
        return "Create failed!"

# link to try: http://127.0.0.1:5000/BookingCreate/11/6?booking_from=2020-12-03&booking_until=2020-12-05


@app.route('/BookingCreate/<int:user_id>/<int:car_id>', methods=['GET'])
@token_required
def hello_booking(current_user, user_id, car_id):
    if current_user.role != 'passenger':
        return jsonify({'message': 'Cannot perform that function!'})
    booking_data = request.args
    booking_controller = BookingController()
    return booking_controller.create(booking_data, user_id, car_id)

# link to try: http://127.0.0.1:5000/CarRead?id=1


@app.route('/CarRead', methods=['GET'])
def read_car():
    car_id = request.args.get('id')
    car_controller = CarController()
    read_car = car_controller.read(car_id)
    return car_controller.read(car_id)

# link to try: http://127.0.0.1:5000/UserRead?id=1


@app.route('/UserRead', methods=['GET'])
@token_required
def read_user(current_user):
    if current_user.role != 'admin':
        return jsonify({'message': 'Cannot perform that function!'})
    user_id = request.args.get('id')
    user_controller = UserController()
    read_user = user_controller.read(user_id)
    return user_controller.read(user_id)

# link to try: http://127.0.0.1:5000/CarsRead


@app.route('/CarsRead', methods=['GET'])
def read_cars():
    car_controller = CarController()
    read_cars = car_controller.read_all()
    output = ""
    for i in range(len(read_cars)):
        output += "Name : " + str(read_cars[i].name) + "   Price : " + str(read_cars[i].price) + "\n"
    return jsonify(message=output, status=200)

# link to try: http://127.0.0.1:5000/NotBookedRead


@app.route('/NotBookedRead', methods=['GET'])
def not_booked_read():
    booking_controller = BookingController()
    read_booking = booking_controller.read()
    car_controller = CarController()
    read_cars = car_controller.read_all()
    output = ""
    for i in range(len(read_cars)):
        k = 1
        for j in range(len(read_booking)):
            a = read_booking[j].car_id
            b = read_cars[i].id
            if a == b:
                k = 0
        if k == 1:
            output += "Name : " + str(read_cars[i].name) + "   Price : " + str(read_cars[i].price) + "\n"
    return output

# link to try: http://127.0.0.1:5000/CarUpdate?id=2&user_id=8&new_price=1234


@app.route('/CarUpdate', methods=['PUT'])
@token_required
def update_car(current_user):
    if current_user.role != 'admin':
        return jsonify({'message': 'Cannot perform that function!'})
    car_id = request.args.get('id')
    car_data = request.args
    car_controller = CarController()
    return car_controller.update_car(car_id, car_data)

# link to try: http://127.0.0.1:5000/CarDelete?id=1&user_id=10&user_id=10


@app.route('/CarDelete', methods=['DELETE'])
@token_required
def delete_car(current_user):
    if current_user.role != 'admin':
        return jsonify({'message': 'Cannot perform that function!'})
    car_id = request.args.get('id')
    user_id = request.args.get('user_id')
    car_controller = CarController()
    return car_controller.delete(car_id, user_id)


# link to try: http://127.0.0.1:5000/UserDelete?id=1


@app.route('/UserDelete', methods=['DELETE'])
@token_required
def delete_user(current_user):
    if current_user.role != 'admin':
        return jsonify({'message': 'Cannot perform that function!'})
    user_id = request.args.get('id')
    user_controller = UserController()
    return user_controller.delete(user_id)


# link to try: http://127.0.0.1:5000/login
@app.route('/login')
def login():
    auth = request.authorization
    user = Users.query.filter_by(first_name=auth['username']).first()
    if not user:
        return jsonify({'message': 'No user found!'})
    if auth.password:
        token = jwt.encode({'id': user.id}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})
    return make_response('Could verify !', 401, {'WWW-authenticate': 'Basic realm="Login Required'})



