import os

from dotenv import load_dotenv
from flask import Flask

from api import manager, customer, auth, menuboard, employee

load_dotenv()

app = Flask(__name__, static_folder=None)

# OAuth2 stuff
app.config['OAUTH2_PROVIDERS'] = {
    # Google OAuth 2.0 documentation:
    # https://developers.google.com/identity/protocols/oauth2/web-server#httprest
    'google': {
        'client_id': os.environ.get('GOOGLE_CLIENT_ID'),
        'client_secret': os.environ.get('GOOGLE_CLIENT_SECRET'),
        'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
        'token_url': 'https://accounts.google.com/o/oauth2/token',
        'userinfo': {
            'url': 'https://www.googleapis.com/oauth2/v3/userinfo',
            'email': lambda json: json['email'],
        },
        'scopes': ['https://www.googleapis.com/auth/userinfo.email'],
    }
}
auth.loginManager.init_app(app)

app.register_blueprint(manager.blueprint, url_prefix='/manager')
app.register_blueprint(customer.blueprint, url_prefix='/')
app.register_blueprint(auth.blueprint, url_prefix='/auth')
app.register_blueprint(menuboard.blueprint, url_prefix='/menuboard')
app.register_blueprint(employee.blueprint, url_prefix='/employee')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
