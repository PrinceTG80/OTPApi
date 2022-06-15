import flask
from flask import request
from authy.api import AuthyApiClient


app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    try: 
        mobile = '9172310389'
        token = request.args['token']

        authy_api = AuthyApiClient(token)

        user = authy_api.users.create(
            email='tgavkhare80@gmail.com',
            phone=mobile,
            country_code=91)

        if user.ok():
            print(user.id)
            # user.id is the `authy_id` needed for future requestscurl 612340182
        else:
            print(user.errors())
        return user.id
    except:
        return  "Hello World"