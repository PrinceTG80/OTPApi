import flask
from flask import request
from authy.api import AuthyApiClient

app = flask.Flask(__name__)
token = 'SFGtP2w2kuBf494bSbmUaRCYeAdEcLHi'
authy_api = AuthyApiClient(token)

@app.route('/', methods = ['GET'])
def home():
    mobile = str(request.arg(['mobile']))
    try: 
        user = authy_api.users.create(
        email='tgavkhare80@gmail.com',
        phone=mobile,
        country_code = 91)
        output = str(user.id)
        if user.ok():
            sms = authy_api.users.request_sms(str(user.id))
            if sms.ok():
                output = str(sms.content)
            return output
        else:
            return "error"
    except:
        return  "Hello World"