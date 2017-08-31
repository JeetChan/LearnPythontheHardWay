""" 
first flask
"""
from flask import Flask
from flask import render_template
from flask import request
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html', title_name='天气查询')


@app.route('/weather', methods=('GET', 'POST'))
def weather():
    if request.method == 'POST':
        order = request.form['order']
        print(order)
    return render_template('index.html', title_name='天气查询')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
