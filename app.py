from flask import Flask, request, jsonify, make_response, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from functools import wraps


app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = '123456789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
db = SQLAlchemy(app)
db.init_app(app)
# db.session.commit()


with app.app_context():
    from routes.posts import *
    from routes.main import *
    from models.models import *

    db.create_all()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)