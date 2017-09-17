"""
输入城市名，获取该城市最新天气情况
点击「帮助」，获取帮助信息
点击「历史」，获取历史查询信息
"""
from flask import Flask
from flask import jsonify
from flask import render_template

from flask import session
from flask_bootstrap import Bootstrap
from WeatherForm import WeatherForm
import weather_servers
from collections import deque
import json
import pickle
from urllib.error import HTTPError
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
bootstrap = Bootstrap(app)
# 加载本地资源
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'weather.sqlite')
app.config.from_object('config')
db = SQLAlchemy(app)


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), unique=True)
    text = db.Column(db.String(50))
    temperature = db.Column(db.String(50))
    wind_direction = db.Column(db.String(50))
    update_time = db.Column(db.String(50))

    def __init__(self, city, text, temperature, wind_direction, update_time):
        self.city = city
        self.text = text
        self.temperature = temperature
        self.wind_direction = wind_direction
        self.update_time = update_time

    def __repr__(self):
        return '<History %r>' % self.city


@app.route('/init')
def init():
    db.create_all()
    return 'Init Successful'


@app.route('/drop')
def drop():
    db.drop_all()
    return 'Drop Successful'


@app.route('/')
def index():
    form = WeatherForm()
    return render_template('index.html', title_name='天气查询', form=form)


@app.route('/search', methods=('GET', 'POST'))
def search_weather():

    form = WeatherForm()
    if form.validate_on_submit():
        try:
            weather_data = {}

            history = History.query.filter_by(city=form.city.data).first()

            if history is not None:
                weather_data = {'city': history.city, 'text': history.text,
                                'temperature': history.temperature, 'wind_direction': history.wind_direction}
            else:
                weather_data = weather_servers.format_weather(form.city.data)
                db.session.add(History(weather_data.get('city'), weather_data.get(
                    'text'), weather_data.get('temperature'), weather_data.get('wind_direction')))
                db.session.commit()

            return jsonify(render_template('weather_data.html', weather_data=weather_data))
        except HTTPError as ex:
            data = {'message': ex.msg}
            return jsonify(render_template('weather_data.html', error=data))

    data = {'message': form.errors['city'][0]}

    return jsonify(render_template('weather_data.html',  data=data))


@app.route('/history', methods=('GET', 'POST'))
def search_history():
    historys = History.query.slice(1, 3)
    if historys is not None:
        return jsonify(render_template('history_data.html', weather_datas=historys))
    else:
        return jsonify(render_template('history_data.html', data={'message': '还没有历史查询记录！'}))


@app.route('/update', methods=('GET', 'POST'))
def update():
    form = WeatherForm()
    if form.validate_on_submit():
        history = History.query.filter_by(
            city=form.city.data.split()[0]).first()
        if history is not None:
            history.text = form.city.data.split()[1]
            db.session.add(history)
            db.session.commit()
    return jsonify(render_template('message_date.html',  data={'message': 'Update Successful'}))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
