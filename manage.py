# manage.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@zerotoone:3306/sakila'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
