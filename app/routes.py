from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/test', methods=['POST'])
def test():

    print(request.get_data())
    return 'testing'