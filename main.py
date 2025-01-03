from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    return redirect(url_for('welcome', name=name))

@app.route('/welcome/<name>')
def welcome(name):
    return f'Login as {name}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
