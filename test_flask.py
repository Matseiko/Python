from flask import url_for
from flask import request, jsonify, make_response

import base64
from app import app_test
import pytest

from templates.routes import token_required

'''
@pytest.fixture(scope='function')
def testapp(app):
    testapp = app_test(app)

    with testapp.app.test_request_context():
        access_token = token_required(identity=Users.query.filter_by(email='victor@gmail.com').first(), expires_delta=False, fresh=True)
    testapp.authorization = ('Bearer', access_token)

    return testapp


def test_read_user(function):
    rv = function.get("/UserRead?id=6")
    assert rv.status_code == 200
'''

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


'''

def test_hello_user_1():
    rv = app_test.get("/UserCreate?email=l000@gmail.com&password=34567&first_name=Lo0&last_name=Lop0&birthday=2001-07-05&role=admin")
    assert rv.get_json() == {
        'message': "The user is created !",
        'status': 200
    }
'''


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


def test_not_booked_read():
    rv = app_test.get("/NotBookedRead")
    assert rv.status_code == 200





# coverage run --omit 'venv/*' -m pytest -q test_flask.py
# coverage report --omit 'venv/*' -m