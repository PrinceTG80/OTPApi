import flask
from flask import request
from authy.api import AuthyApiClient


app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    try: 
        mobile = request.args['mobile']
        token = 'SFGtP2w2kuBf494bSbmUaRCYeAdEcLHi'

        authy_api = AuthyApiClient(token)

        user = authy_api.users.create(
            email='tgavkhare80@gmail.com',
            phone=mobile,
            country_code=91)

        if user.ok():
            print(user.id)
            return user.id
        else:
            return user.errors()
    except:
        return  "Hello World"