import secrets
from urllib.parse import urlencode

import requests as requests
from flask import Blueprint, render_template, redirect, url_for, current_app, abort, session, request, flash
from flask_login import LoginManager, current_user, login_user, logout_user

from .user import User
from .auth_helper import getUserByEmail, createUser, getUserById

"""
CREDIT: https://blog.miguelgrinberg.com/post/oauth-authentication-with-flask-in-2023
"""

authBlueprint = Blueprint("auth", __name__, template_folder="templates")
loginManager = LoginManager()


@loginManager.user_loader
def load_user(user_id) -> User | None:
    print(f"{user_id = }")
    return getUserById(user_id)


@authBlueprint.route("/")
def home():
    print(f"{current_user = }")
    return render_template("login.html")


@authBlueprint.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("auth.home"))


@authBlueprint.route("/<provider>")
def oauth2_authorize(provider: str):
    if not current_user.is_anonymous:
        return redirect(url_for('customer.home'))

    provider_data = current_app.config['OAUTH2_PROVIDERS'].get(provider)
    if provider_data is None:
        abort(404)

    # generate a random string for the state parameter
    session['oauth2_state'] = secrets.token_urlsafe(16)

    # generate a random string for the state parameter
    session['oauth2_state'] = secrets.token_urlsafe(16)

    # create a query string with all the OAuth2 parameters
    qs = urlencode({
        'client_id': provider_data['client_id'],
        'redirect_uri': url_for('auth.oauth2_callback', provider=provider,
                                _external=True),
        'response_type': 'code',
        'scope': ' '.join(provider_data['scopes']),
        'state': session['oauth2_state'],
    })

    # redirect the user to the OAuth2 provider authorization URL
    return redirect(provider_data['authorize_url'] + '?' + qs)


@authBlueprint.route('/callback/<provider>')
def oauth2_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('customer.home'))

    provider_data = current_app.config['OAUTH2_PROVIDERS'].get(provider)
    if provider_data is None:
        abort(404)

    # if there was an authentication error, flash the error messages and exit
    if 'error' in request.args:
        for k, v in request.args.items():
            if k.startswith('error'):
                flash(f'{k}: {v}')
        return redirect(url_for('customer.home'))

    # make sure that the state parameter matches the one we created in the
    # authorization request
    if request.args['state'] != session.get('oauth2_state'):
        abort(401)

    # make sure that the authorization code is present
    if 'code' not in request.args:
        abort(401)

    # exchange the authorization code for an access token
    response = requests.post(provider_data['token_url'], data={
        'client_id': provider_data['client_id'],
        'client_secret': provider_data['client_secret'],
        'code': request.args['code'],
        'grant_type': 'authorization_code',
        'redirect_uri': url_for('auth.oauth2_callback', provider=provider,
                                _external=True),
    }, headers={'Accept': 'application/json'})
    if response.status_code != 200:
        abort(401)
    oauth2_token = response.json().get('access_token')
    if not oauth2_token:
        abort(401)

    # use the access token to get the user's email address
    response = requests.get(provider_data['userinfo']['url'], headers={
        'Authorization': 'Bearer ' + oauth2_token,
        'Accept': 'application/json',
    })
    if response.status_code != 200:
        abort(401)
    email = provider_data['userinfo']['email'](response.json())

    # find or create the user in the database
    user = getUserByEmail(email)
    if user is None:
        user = createUser(email)

    # log the user in
    print(f"{user = }")
    login_status = login_user(user)
    print(f"{login_status = }")
    # TODO :: Add options for employee or manager to go to their pages
    return redirect(url_for('customer.home'))
