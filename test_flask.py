from flask import url_for
from flask import request, jsonify, make_response

import base64
from app import app_test, app_log
import pytest
import jwt
from Models.ModelUsers import Users
from datetime import datetime, timedelta
from templates.routes import token_user


@pytest.fixture()
def admin():
    app = app_log()
    app.app_context().push()
    app.testing = True
    client = app.test_client()
    global token
    user_id = Users.query.filter_by(first_name="Victor").first().id
    token = jwt.encode({'id': user_id}, app.config['SECRET_KEY'])
    yield client
    app.testing = False


@pytest.fixture()
def passenger():
    app = app_log()
    app.app_context().push()
    app.testing = True
    client = app.test_client()
    global token
    user_id = Users.query.filter_by(first_name="Vova").first().id
    token = jwt.encode({'id': user_id}, app.config['SECRET_KEY'])
    yield client
    app.testing = False


def test_hello():
    rv = app_test.get("/start")
    assert rv.get_json() == {
        'message': 'Hello world !',
        'status': 200
    }


def test_login_1():
    log = base64.b64encode(b'Victor:').decode('utf-8')
    rv = app_test.get('/login', headers={'Authorization': 'Basic ' + log})
    assert rv.status_code == 401


def test_login_2():
    log = base64.b64encode(b'Victor:6666').decode('utf-8')
    res = app_test.get('/login', headers={'Authorization': 'Basic ' + log})
    assert res.status_code == 200


def test_login_3():
    log = base64.b64encode(b'Voo:6666').decode('utf-8')
    rv = app_test.get('/login', headers={'Authorization': 'Basic ' + log})
    assert rv.get_json() == {
        'message': "No user found!",
    }


def test_hello_user_1():
    rv = app_test.get("/UserCreate?email=l000@gmail.com&password=34567&first_name=Lo0&last_name=Lop0&birthday=2001-07-05&role=admin")
    assert rv.get_json() == {
        'message': "The user is created !",
        'status': 200
    }


def test_hello_user_2():
    rv = app_test.get("/UserCreate?password=23456&first_name&last_name=Lolip&birthday=2000-07-03&role=admin")
    assert rv.get_json() == {
        'message': "Error!",
        'status': 400
    }


def test_hello_user_3():
    rv = app_test.get("/UserCreate?email=viko@gmail.com&password=34568&first_name=vi&last_name=&birthday=2001-07-21&role=admin")
    assert rv.get_json() == {
        'message': "Missing values !",
        'status': 404
    }


def test_read_user_1(admin):
    headers = {'x-access-token': token}
    rv = app_test.get("/UserRead?id=8", headers=headers)
    assert rv.status_code == 200


def test_read_user_2(admin):
    headers = {'x-access-token': token}
    rv = app_test.get("/UserRead?id=100", headers=headers)
    assert rv.get_json() == {
        'message': "The user was not found !",
        'status': 404
    }


def test_delete_user_1(admin):
    headers = {'x-access-token': token}
    rv = app_test.delete("/UserDelete?id=100", headers=headers)
    assert rv.get_json() == {
        'message': "The user was not found !",
        'status': 404
    }


def test_delete_user_2(admin):
    headers = {'x-access-token': token}
    rv = app_test.delete("/UserDelete?id=19", headers=headers)
    assert rv.get_json() == {
        'message': "User was deleted !",
        'status': 200
    }


def test_hello_car_1(admin):
    headers = {'x-access-token': token}
    rv = app_test.get("/CarCreate?name=&price=100", headers=headers)
    assert rv.get_json() == {
        'message': "Missing values !",
        'status': 404
    }


def test_hello_car_2(admin):
    headers = {'x-access-token': token}
    rv = app_test.get("/CarCreate?name=Irr&price=100", headers=headers)
    assert rv.get_json() == {
        'message': "The car is created !",
        'status': 200
    }


def test_hello_car_1_token():
    rv = app_test.get("/CarCreate?name=BMW&price=100")
    assert rv.get_json() == {
        'message': "Token is missing !"
    }


def test_read_car_1():
    rv = app_test.get("/CarRead?id=100")
    assert rv.get_json() == {
        'message': "The car was not found",
        'status': 404
    }


def test_read_car_2():
    rv = app_test.get("/CarRead?id=2")
    assert rv.status_code == 200


def test_read_cars():
    rv = app_test.get("/CarsRead")
    assert rv.status_code == 200


def test_update_car_1(admin):
    headers = {'x-access-token': token}
    rv = app_test.put("/CarUpdate?id=2&user_id=8&new_price=", headers=headers)
    assert rv.get_json() == {
        'message': "Missing values !",
        'status': 404
    }


def test_update_car_2(admin):
    headers = {'x-access-token': token}
    rv = app_test.put("/CarUpdate?id=2&user_id=8&new_price=123", headers=headers)
    assert rv.get_json() == {
        'message': "Car was updated !",
        'status': 200
    }


def test_delete_car_1(admin):
    headers = {'x-access-token': token}
    rv = app_test.delete("/CarDelete?id=1000", headers=headers)
    assert rv.get_json() == {
        'message': "The car was not found !",
        'status': 404
    }


def test_delete_car_2(admin):
    headers = {'x-access-token': token}
    rv = app_test.delete("/CarDelete?id=17", headers=headers)
    assert rv.get_json() == {
        'message': "Car was deleted !",
        'status': 200
    }


def test_hello_booking_1(passenger):
    headers = {'x-access-token': token}
    rv = app_test.get("/BookingCreate/15/7?booking_from=&booking_until=2020-12-05", headers=headers)
    assert rv.get_json() == {
        'message': "ERROR",
        'status': 400
    }


def test_hello_booking_2(passenger):
    headers = {'x-access-token': token}
    rv = app_test.get("/BookingCreate/15/9?booking_from=2020-12-03&booking_until=2020-12-05", headers=headers)
    assert rv.get_json() == {
        'message': "The booking is created !",
        'status': 200
    }


def test_not_booked_read():
    rv = app_test.get("/NotBookedRead")
    assert rv.status_code == 200


# coverage run --omit 'venv/*' -m pytest -q test_flask.py
# coverage report --omit 'venv/*' -m
