from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

# remember to change to heroku's databas
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lab7@localhost/lab7"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://"
db = SQLAlchemy(app)




