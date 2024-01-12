from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix
from sqlalchemy.orm import DeclarativeBase
# from models import db

app =Flask(__name__)

class Base(DeclarativeBase):
  pass

app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.root_path}/questions.sqlite"
app.config['CORS_METHODS'] = ['GET', 'POST', 'PUT', 'DELETE']

# app.wsgi_app = ProxyFix(
#     app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
# )

@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify ({
        'message': "Hello World!"
    })

db = SQLAlchemy(model_class=Base)    

import models

db.init_app(app)


with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)


