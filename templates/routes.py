from flask import request
from app import app

from Controller.UserController import UserController
from Controller.CarController import CarController
from Controller.BookingController import BookingController


@app.route("/start")
def hello():
    return "Hello world !"

# link to try: http://127.0.0.1:5000/UserCreate?email=vika@gmail.com&password=11111&first_name=Vika&last_name=Oh&birthday=2002-07-08&role=admin


@app.route('/UserCreate', methods=['GET'])
def hello_user():
    user_data = request.args
    user_controller = UserController()
    if user_controller.create(user_data):
        return "Success!"
    else:
        return "Create failed!"

# link to try: http://127.0.0.1:5000/CarCreate?name=BMW&price=100


@app.route('/CarCreate', methods=['GET'])
def hello_car():
    car_data = request.args
    car_controller = CarController()
    if car_controller.create(car_data):
        return "Success!"
    else:
        return "Create failed!"

# link to try: http://127.0.0.1:5000/BookingCreate/11/6?booking_from=2020-12-03&booking_until=2020-12-05


@app.route('/BookingCreate/<int:user_id>/<int:car_id>', methods=['GET'])
def hello_booking(user_id, car_id):
    booking_data = request.args
    booking_controller = BookingController()
    return booking_controller.create(booking_data, user_id, car_id)

# link to try: http://127.0.0.1:5000/CarRead?id=1


@app.route('/CarRead', methods=['GET'])
def read_car():
    car_id = request.args.get('id')
    car_controller = CarController()
    read_car = car_controller.read(car_id)
    #return "Name : " + str(read_car.name) + "   Price : " + str(read_car.price)
    return car_controller.read(car_id)

# link to try: http://127.0.0.1:5000/UserRead?id=1


@app.route('/UserRead', methods=['GET'])
def read_user():
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
    return output

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
def update_car():
    car_id = request.args.get('id')
    car_data = request.args
    car_controller = CarController()
    return car_controller.update_car(car_id, car_data)

# link to try: http://127.0.0.1:5000/CarDelete?id=1&user_id=10&user_id=10


@app.route('/CarDelete', methods=['DELETE'])
def delete_car():
    car_id = request.args.get('id')
    user_id = request.args.get('user_id')
    car_controller = CarController()
    return car_controller.delete(car_id, user_id)


# link to try: http://127.0.0.1:5000/UserDelete?id=1


@app.route('/UserDelete', methods=['DELETE'])
def delete_user():
    user_id = request.args.get('id')
    user_controller = UserController()
    return user_controller.delete(user_id)