import os
import smtplib

from celery import Celery
from flask import (
    Flask,
    request,
    render_template,
)
import requests
import time

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = os.environ['REDIS_URL']

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'],
    backend=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

EMAIL_SENDER = os.environ.get('MAIL_USERNAME')
EMAIL_SENDER_PASSWD = os.environ.get('MAIL_PASSWORD')


@celery.task()
def add(x, y):
    return x + y


@celery.task()
def make_request():
    requests.get('http://httpbin.org/delay/5')


@celery.task()
def send_invitation_email(email):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(EMAIL_SENDER, EMAIL_SENDER_PASSWD)
    subject = 'Python Level Up'
    text = 'Welcome to Python Level Up Sample Website!'
    body = '\r\n'.join(
        [
            'To: %s' % email,
            'From: %s' % EMAIL_SENDER,
            'Subject: %s' % subject,
            '', text
        ]
    )
    server.sendmail(EMAIL_SENDER, [email], body)


@app.route('/sync_request')
def make_sync_request():
    start = time.time()
    make_request()
    end = time.time()
    return str(end - start)

    
@app.route('/async_request')
def make_async_request():
    start = time.time()
    make_request.delay()
    end = time.time()
    return str(end - start)


@app.route('/wait')
def wait_for_result():
    result = add.delay(3, 5).get()
    return str(result)


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        email = request.form['email']
        send_invitation_email.delay(email)
        return 'Konto założone'
    else:
        return render_template('add_user.html')


if __name__ == '__main__':
    app.run(debug=True)
