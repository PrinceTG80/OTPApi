import flask
from flask import request
from authy.api import AuthyApiClient

app = flask.Flask(__name__)
token = 'SFGtP2w2kuBf494bSbmUaRCYeAdEcLHi'
authy_api = AuthyApiClient(token)
mobile = '9172310389'
user = authy_api.users.create(
        email='tgavkhare80@gmail.com',
        phone=mobile,
        country_code = 91)
output = str(user.id)
@app.route('/', methods = ['GET'])
def home():
    try: 
        if user.ok():
            return output
        else:
            return "error"
    except:
        return  "Hello World"