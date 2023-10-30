from flask import Flask, render_template

from api import manager, customer, auth, menuboard, employee

app = Flask(__name__)
app.register_blueprint(manager.blueprint, url_prefix='/manager')
app.register_blueprint(customer.blueprint, url_prefix='/')
app.register_blueprint(auth.blueprint, url_prefix='/auth')
app.register_blueprint(menuboard.blueprint, url_prefix='/menuboard')
app.register_blueprint(employee.blueprint, url_prefix='/employee')

app.static_url_path = '/static'
app.static_folder = 'static'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
