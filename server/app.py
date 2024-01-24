from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix
from sqlalchemy.orm import DeclarativeBase
import routes
from flask_cors import CORS

app =Flask(__name__)
CORS(app) 

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

from models import *

@app.route('/api/papers')
def get_paper_names():
    papers = Paper_Name.query.all()
    # paper_names = [paper.Paper_Name for paper in papers]
    paper_names = [{ 'paper_id': paper.Paper_ID, 'paper_name': paper.Paper_Name} for paper in papers]
    return jsonify(paper_names)


@app.route('/api/questions', methods=['GET'])
def get_questions():
    questions = Questions.query.all()
    question_data = [{'id': question.QiD, 'question_string': question.Question_String} for question in questions]
    return jsonify(question_data)


@app.route('/api/topics', methods=['GET'])
def get_topics():
    topics = Topics.query.all()
    topic_data = [{'id': topic.Topic_ID, 'topic_name': topic.Topic_Name, 'component_id': topic.Component_of_Paper_ID} for topic in topics]
    return jsonify(topic_data)


@app.route('/api/component', methods=['GET'])
def get_components():
    components = Component_of_Paper.query.all()
    component_data = [{'component_id': component.Component_of_Paper_ID, 'component_name': component.Component_Name, 'marks': component.Marks, 'paper_id': component.Paper_ID} for component in components]
    return jsonify(component_data)


db.init_app(app)


with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)


