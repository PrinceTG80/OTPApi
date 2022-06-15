import flask
from flask import request
from authy.api import AuthyApiClient

app = flask.Flask(__name__)


@app.route('/', methods = ['GET'])
def home():
    token = str(request.args['token'])
    authy_api = AuthyApiClient(token)
    mobile = str(request.args['mobile'])
    try: 
        user = authy_api.users.create(
        email='user@gmail.com',
        phone=mobile,
        country_code = 91)
        output = str(user.id)
        if user.ok():
            sms = authy_api.users.request_sms(str(user.id), {'display_name': str(user.id)})
            output = '{"output" : '+ output +''}'
            return output
        else:
            return "error"
    except:
        return  "Hello World"