from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app =Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.root_path}/cards.sqlite"
app.config['CORS_METHODS'] = ['GET', 'POST', 'PUT', 'DELETE']

# from werkzeug.middleware.proxy_fix import ProxyFix

# app.wsgi_app = ProxyFix(
#     app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
# )


from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)


db = SQLAlchemy()    

db.init_app(app)

with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run()


