import flask
from flask import request
from authy.api import AuthyApiClient


app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    mobile = '9172310389'
    token = 'SFGtP2w2kuBf494bSbmUaRCYeAdEcLHi'

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
    return  "Hello World"