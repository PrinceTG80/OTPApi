import flask
from flask import request
from authy.api import AuthyApiClient

token = 'SFGtP2w2kuBf494bSbmUaRCYeAdEcLHi'
authy_api = AuthyApiClient(token)

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    try: 
        mobile = '9172310389'
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