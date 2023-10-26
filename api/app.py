from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET'])
def customerHome():
    return render_template('customer_home.html')


@app.route("/login", methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/manager')
def managerHome():
    return render_template('manager_home.html')


@app.route('/employee')
def employeeHome():
    return render_template('employee_home.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
