from random import choice

from flask import Flask
from flask_celery import make_celery
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'db+postgresql://keith_njagi:kitgiana@172.17.0.1/my_celery_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://keith_njagi:kitgiana@172.17.0.1/my_celery_db'

celery = make_celery(app)
db = SQLAlchemy(app)

class Results(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    data =db.Column('data', db.String(80))

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/process/<name>')
def process(name):

    reverse.delay(name)

    return 'I sent an async request!'

@app.route('/insertData')
def insertDate():
    insert.delay()
    return 'I sent an async request to insert data into the database.'

@celery.task(name='celery_example.reverse')
def reverse(string):
    return string[::-1]

@celery.task(name='celery_example.insert')
def insert():
    for i in range(500):
        data = ''.join(choice('ABCDE') for i in range(10))
        result = Results(data=data)

        db.session.add(result)

    db.session.commit()
    return 'Done!!'


if __name__ == '__main__':
    app.run(debug=True)