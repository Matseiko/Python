from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from Database import db, bcrypt
from Manager import manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
JWT_HEADER_TYPE = 'Bearer'
JWT_BLACKLIST_ENABLED = False
from templates import routes

#app.secret_key = 'secret_key'

app.config['SECRET_KEY'] = 'secret_key'
db.init_app(app)
manager.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

app_test = app.test_client()

if __name__ == '__main__':
    app.run()

